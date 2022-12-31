""" Global variables of the macro are collected here """

import pathlib
from PySide.QtGui import QFileDialog, QApplication  # FreeCAD's PySide
import FreeCAD as App


g_param = App.ParamGet('User parameter:Plugins/cadbase_library')
g_api_login = 'https://api.cadbase.rs/login'
g_cdbs_api = 'https://api.cadbase.rs/graphql'
g_program_id = 42  # this is FreeCAD ID in CADBase
g_user_agent = b'Mozilla/5.0 (Macintosh; Intel Mac OS 10 12.3; rv:42.0) \
                Gecko/20100101 Firefox/42.0'
g_content_type = b'application/json'
g_ui_file = App.getUserMacroDir(True) + '/CadbaseLibrary/cadbase_library.ui'
g_ui_file_config = App.getUserMacroDir(True) + '/CadbaseLibrary/cadbase_library_config.ui'
g_len_uuid = 36  # for a little uuid validation
g_library_path = g_param.GetString('destination')  # for save the path to the local CADBase library


def set_library_path():
    """ Getting the location for the CADBase library,
    if the value is empty or invalid, the existing location is requested from the user """
    global g_library_path
    destination = g_param.GetString('destination')
    if destination and pathlib.Path(destination).is_dir():
        return destination
    new_destination = \
        QFileDialog.getExistingDirectory(None, QApplication.translate('CADBaseLibrary',
                                                                      'Location of your existing CADBase library'))
    # forward slashes apparently work on windows too
    g_param.SetString('destination', new_destination.replace('\\', '/'))
    g_library_path = g_param.GetString('destination')
    return g_library_path


def set_base_param():
    """ Setting default options if they weren't set before """
    if not g_param.GetString('api-url'):
        g_param.SetString('api-url', g_cdbs_api)
    if not g_param.GetString('auth-token'):
        g_param.SetString('auth-token', '')


set_library_path()  # update library path
# Please don't use this name as the name of files or folders in the CADBase Library folder.
g_response_path = pathlib.Path(g_library_path) / 'cadbase_response_file_2018'
g_log_file_path = g_response_path.with_suffix('.log')
