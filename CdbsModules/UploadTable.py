from PySide import QtGui, QtCore  # FreeCAD's PySide
import FreeCADGui as Gui
from CdbsModules.Translate import translate


class TableUploadFiles(QtCore.QAbstractTableModel):
    def __init__(self, items):
        super().__init__()
        self.items = items
        self.headers = [
            translate('CdbsStorage', 'Filename'),
            translate('CdbsStorage', 'Size (local)'),
            translate('CdbsStorage', 'Date modified'),
            translate('CdbsStorage', 'Size (remote)'),
            translate('CdbsStorage', 'Upload date'),
            translate('CdbsStorage', 'Status')
        ]

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            return self.items[index.row()][index.column()]

    def rowCount(self, index):
        return len(self.items)

    def columnCount(self, index):
        if self.items:
            return len(self.items[0])
        return 0

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.headers[col]
        return None