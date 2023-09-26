# ***************************************************************************
# *                                                                         *
# *   Copyright (c) 2022 mnnxp <in@cadbase.rs>                              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************

""" This code to integrate FreeCAD with CADBase.
The macro is designed to load and use components (parts) from CADBase in the FreeCAD interface. """

import zipfile
import tempfile
import pathlib
from pathlib import Path
from types import SimpleNamespace
from PySide import QtGui, QtCore  # FreeCAD's PySide
import Part
import FreeCADGui as Gui
import CdbsModules.CdbsEvn
from CdbsModules.CdbsAuth import CdbsAuth
from CdbsModules.CdbsApi import CdbsApi
from CdbsModules.CdbsStorage import CdbsStorage
from CdbsModules.QueriesApi import QueriesApi
import CdbsModules.DataHandler as DataHandler
from CdbsModules.Translate import translate

try:
    QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName('UTF-8'))
except Exception as e:
    DataHandler.logger('log', f'Will fall back to Latin-1: {e}')
try:
    CdbsModules.CdbsEvn.set_library_path()  # get the location for the CADBase library
except Exception as e:
    DataHandler.logger(
        'error',
        translate('CadbaseMacro', 'Failed to set path for local library:')
        + f' {e}',
    )
try:
    CdbsModules.CdbsEvn.set_base_param()  # set default options if they weren't set before
    CdbsModules.CdbsEvn.update_api_points()  # update api points (in case a non-official server is used)
except Exception as e:
    DataHandler.logger(
        'error',
        translate('CadbaseMacro', 'Failed with settings base parameters:')
        + f' {e}',
    )
g_selected_component_uuid: str = ''
g_selected_modification_uuid: str = ''
g_last_clicked_object: Path = Path('')


class ExpFileSystemModel(QtGui.QFileSystemModel):
    """A custom QFileSystemModel that displays freecad file icons"""

    def __init__(self):
        QtGui.QFileSystemModel.__init__(self)

    def data(self, index, role):
        if index.column() == 0 and role == QtCore.Qt.DecorationRole:
            if index.data().lower().endswith('.fcstd'):
                return QtGui.QIcon(':icons/freecad-doc.png')
            elif index.data().lower() == 'private':
                return QtGui.QIcon.fromTheme('folder-lock')
        return super(ExpFileSystemModel, self).data(index, role)


class ExpCdbsWidget(QtGui.QDockWidget):
    """A library explorer CADBase widget"""

    def __init__(self):
        QtGui.QDockWidget.__init__(self)
        self.setObjectName('CADBaseLibrary')
        self.setWindowTitle(translate("InitGui", "CADBase Library"))
        self.form = Gui.PySideUic.loadUi(CdbsModules.CdbsEvn.g_ui_file)
        self.dirmodel = ExpFileSystemModel()
        self.dirmodel.setRootPath(CdbsModules.CdbsEvn.g_library_path)
        self.dirmodel.setNameFilters(
            [
                '*.fcstd',
                '*.FcStd',
                '*.FCSTD',
                '*.stp',
                '*.STP',
                '*.step',
                '*.STEP',
                '*.brp',
                '*.BRP',
                '*.brep',
                '*.BREP',
            ]
        )
        self.dirmodel.setNameFilterDisables(0)
        self.form.folder.setModel(self.dirmodel)
        self.form.folder.hideColumn(1)
        self.form.folder.hideColumn(2)
        self.form.folder.hideColumn(3)
        self.form.folder.setRootIndex(self.dirmodel.index(CdbsModules.CdbsEvn.g_library_path))

        self.previewframe = self.form.toolBox.widget(0)
        self.previewframe.preview = \
            self.previewframe.findChild(QtGui.QLabel, 'preview')
        self.optbuttons = self.form.toolBox.widget(1)
        self.optbuttons.updatebutton = \
            self.optbuttons.findChild(QtGui.QToolButton, 'updatebutton')
        self.optbuttons.uploadbutton = \
            self.optbuttons.findChild(QtGui.QToolButton, 'uploadbutton')
        self.optbuttons.configbutton = \
            self.optbuttons.findChild(QtGui.QToolButton, 'configbutton')
        self._connect_widgets()
        self.setWidget(self.form)

    def _connect_widgets(self):
        self.form.folder.clicked.connect(self.clicked)
        self.form.folder.doubleClicked.connect(self.doubleclicked)
        self.optbuttons.updatebutton.clicked.connect(self.update_library)
        self.optbuttons.uploadbutton.clicked.connect(self.upload_files)
        self.optbuttons.configbutton.clicked.connect(self.setconfig)

    def clicked(self, index):
        global g_last_clicked_object
        g_last_clicked_object = pathlib.Path(self.dirmodel.filePath(index))
        self.previewframe.preview.clear()  # clear preview frame
        if g_last_clicked_object.suffix.lower() == '.fcstd':
            self.set_preview_img()
        if g_last_clicked_object.is_dir():
            update_selected_object_uuid()

    def doubleclicked(self, index):
        global g_last_clicked_object
        g_last_clicked_object = pathlib.Path(self.dirmodel.filePath(index))
        if not g_last_clicked_object.is_dir():
            self.add_part()
            return
        if not CdbsModules.CdbsEvn.g_param.GetString('auth-token'):
            DataHandler.logger('error', translate('CadbaseMacro', "Token not found"))
            return
        # user-clicked was on directory, need updating uuid of selected component or modification
        update_selected_object_uuid()
        if g_selected_component_uuid:
            update_component()
            return
        if g_selected_modification_uuid:
            update_component_modificaion()

    def update_library(self):
        update_components_list()

    def upload_files(self):
        arg = (g_selected_modification_uuid, g_last_clicked_object)
        CdbsStorage(arg)

    def setconfig(self):
        ConfigDialog(parent=self)

    def add_part(self):
        """Adding a part to an open document or in a new one"""
        DataHandler.logger('message', translate('CadbaseMacro', 'Processing the part...'))
        str_path = str(g_last_clicked_object.resolve())
        path_suffix = g_last_clicked_object.suffix.lower()
        try:
            if (
                path_suffix == '.stp'
                or path_suffix == '.step'
                or path_suffix == '.brp'
                or path_suffix == '.brep'
            ):
                Part.show(Part.read(str_path))
            elif path_suffix == '.fcstd':
                Gui.activeDocument().mergeProject(str_path)
            Gui.SendMsgToActiveView('ViewFit')
        except Exception as e:
            DataHandler.logger('error', str(e))
            return

    def set_preview_img(self):
        """Setting image in preview tab (trying to get image of FreeCAD file)"""
        try:
            zfile = zipfile.ZipFile(g_last_clicked_object)
            files = zfile.namelist()
            # check for meta-file if it's really a FreeCAD document
            if not files[0] == 'Document.xml':
                return
            DataHandler.logger('log', translate('CadbaseMacro', 'Processing for preview the part...'))
            image = 'thumbnails/Thumbnail.png'
            if image in files:
                image = zfile.read(image)
                thumbfile = tempfile.mkstemp(suffix='.png')[1]
                thumb = open(thumbfile, 'wb')
                thumb.write(image)
                thumb.close()
                im = QtGui.QPixmap(thumbfile)
                self.previewframe.preview.setPixmap(im)
        except Exception as e:
            DataHandler.logger('error', f'{e}: {g_last_clicked_object}')
            self.previewframe.preview.clear()  # clear preview in case of any error


class ConfigDialog(QtGui.QDialog):
    """A dialog for macro settings and get access token"""

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setObjectName('CADBaseLibraryConfig')
        self.setWindowTitle(translate('CadbaseMacro', "CADBase Library Configuration"))
        self.form = Gui.PySideUic.loadUi(CdbsModules.CdbsEvn.g_ui_file_config)
        self._connect_widgets()
        self.form.show()
        self.form.lineEdit_3.setText(CdbsModules.CdbsEvn.g_param.GetString('destination', ''))
        self.form.lineEdit.setText(CdbsModules.CdbsEvn.g_param.GetString('api-url', ''))

    def _connect_widgets(self):
        self.form.buttonBox.accepted.connect(self.accept)
        self.form.buttonBox.rejected.connect(self.reject)
        self.form.pushButton.clicked.connect(self.setdefaulturl)
        self.form.pushButton_3.clicked.connect(self.changepath)

    def setdefaulturl(self):
        self.form.lineEdit.setText(CdbsModules.CdbsEvn.g_base_api)

    def changepath(self):
        CdbsModules.CdbsEvn.g_library_path = \
            CdbsModules.CdbsEvn.g_param.GetString('destination', '')
        np = QtGui.QFileDialog.getExistingDirectory(
            self,
            translate(
                'CadbaseMacro',
                'Local location of your existing CADBase library',
            ),
            CdbsModules.CdbsEvn.g_library_path,
        )
        if np:
            self.form.lineEdit_3.setText(np)

    def reject(self):
        DataHandler.logger('message', translate('CadbaseMacro', 'Changes not accepted'))
        self.form.close()

    def accept(self):
        if self.form.lineEdit.text():
            CdbsModules.CdbsEvn.g_param.SetString('api-url', self.form.lineEdit.text())
            CdbsModules.CdbsEvn.update_api_points()
        if self.form.lineEdit_3.text() != CdbsModules.CdbsEvn.g_library_path:
            CdbsModules.CdbsEvn.g_param.SetString('destination', self.form.lineEdit_3.text())
            DataHandler.logger('warning', translate('CadbaseMacro', 'Please restart FreeCAD'))
        if self.form.lineEdit_2.text() and self.form.lineEdit_4.text():
            username = self.form.lineEdit_2.text()
            password = self.form.lineEdit_4.text()
            CdbsAuth(username, password)
        DataHandler.logger('message', translate('CadbaseMacro', 'Configuration updated'))
        self.form.close()


if QtCore.QDir(CdbsModules.CdbsEvn.g_library_path).exists():
    m = Gui.getMainWindow()
    w = m.findChild(QtGui.QDockWidget, 'CADBaseLibrary')
    if w and hasattr(w, 'isVisible'):
        if w.isVisible():
            w.hide()
        else:
            w.show()
    else:
        m.addDockWidget(QtCore.Qt.RightDockWidgetArea, ExpCdbsWidget())
else:
    DataHandler.logger(
        'warning',
        translate('CadbaseMacro', "Library path not found:")
        + f' "{CdbsModules.CdbsEvn.g_library_path}"',
    )


def update_components_list():
    """Create folders for all bookmark components of the current user"""
    CdbsApi(QueriesApi.fav_components())
    data = DataHandler.parsing_gpl()
    if not isinstance(data, SimpleNamespace):
        DataHandler.logger(
            'warning',
            translate(
                'CadbaseMacro',
                'Received data about components is not suitable for processing',
            ),
        )
        return
    if not data.components:
        DataHandler.logger('warning', translate('CadbaseMacro', "You don't have favorite components"))
        return
    for component in data.components:
        DataHandler.logger(
            'log',
            translate('CadbaseMacro', 'Component UUID:')
            + f' {component.uuid}',
        )
        new_dir: Path = (
            pathlib.Path(CdbsModules.CdbsEvn.g_library_path)
            / f'{component.name} (from  {component.ownerUser.username})'
        )
        DataHandler.create_object_path(new_dir, component, 'component')
    DataHandler.logger('message', translate('CadbaseMacro', 'Component list update finished'))


def update_component():
    """Creating folders for all component modifications of current component"""
    if not g_selected_component_uuid:
        DataHandler.logger('warning', translate('CadbaseMacro', 'Not set UUID for select component'))
        return
    CdbsApi(QueriesApi.component_modifications(g_selected_component_uuid))
    data = DataHandler.parsing_gpl()
    if not isinstance(data, SimpleNamespace):
        DataHandler.logger(
            'warning',
            translate(
                'CadbaseMacro',
                'Received data about component is not suitable for processing'
            ),
        )
        return
    if not data.componentModifications:
        DataHandler.logger('warning', translate('CadbaseMacro', 'No modifications for the component'))
    for modification in data.componentModifications:
        new_dir = g_last_clicked_object / modification.modificationName
        DataHandler.create_object_path(new_dir, modification, 'modification')
    DataHandler.logger('message', translate('CadbaseMacro', 'Updated the list of component modifications'))


def update_component_modificaion():
    """Updating files on modification folder"""
    if not g_selected_modification_uuid:
        DataHandler.logger('warning', translate('CadbaseMacro', 'Not set UUID for select modification'))
        return
    CdbsApi(QueriesApi.target_fileset(g_selected_modification_uuid))
    data = DataHandler.parsing_gpl()
    if not isinstance(data, SimpleNamespace):
        DataHandler.logger('warning', translate('CadbaseMacro', 'Received data about fileset is not suitable for processing'))
        return
    if not data.componentModificationFilesets:
        DataHandler.logger('warning', translate('CadbaseMacro', 'Fileset not found for FreeCAD'))
        return
    CdbsApi(QueriesApi.fileset_files(data.componentModificationFilesets[0].uuid))
    data = DataHandler.parsing_gpl()
    if not isinstance(data, SimpleNamespace):
        DataHandler.logger(
            'warning',
            translate(
                'CadbaseMacro',
                'Received data about files of fileset is not suitable for processing',
            ),
        )
        return
    if not data.componentModificationFilesetFiles:
        DataHandler.logger('warning', translate('CadbaseMacro', 'No files in fileset'))
        return
    # necessary data to start downloading files
    urls = []  # for store pre-signed URLs for downloading files
    fns = []  # for store full patches with filenames
    for file_of_fileset in data.componentModificationFilesetFiles:
        urls.append(file_of_fileset.downloadUrl)
        fns.append(g_last_clicked_object / file_of_fileset.filename)
    inputs = zip(urls, fns)
    DataHandler.download_parallel(inputs)
    DataHandler.logger('message', translate('CadbaseMacro', 'Download file(s):') + f' {len(urls)}')
    DataHandler.logger('message', translate('CadbaseMacro', 'Component modification files update completed'))


def update_selected_object_uuid():
    """Upgrading selected uuid for a object, get data from user-selected a folder"""
    global g_selected_component_uuid
    global g_selected_modification_uuid
    # clearing old uuids
    g_selected_component_uuid = ''
    g_selected_modification_uuid = ''
    component_file = g_last_clicked_object / 'component'
    # check file with component info
    if component_file.exists():
        component_data = DataHandler.read_object_info(component_file, 'component')
        g_selected_component_uuid = component_data.uuid
        return
    modification_file = g_last_clicked_object / 'modification'
    # check file with modification info
    if modification_file.exists():
        modification_data = DataHandler.read_object_info(modification_file, 'modification')
        # save the uuid of the selected modification for uploading files
        g_selected_modification_uuid = modification_data.uuid
