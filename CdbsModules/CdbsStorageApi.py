"""Functionality for processing requests to the storage (S3) of CADBase platform"""

from PySide import QtCore, QtNetwork  # FreeCAD's PySide
from PySide.QtCore import QFile  # FreeCAD's PySide
import CdbsModules.DataHandler as DataHandler
from CdbsModules.Translate import translate


class CdbsStorageApi:
    """Sending a file to CADBase storage and handling response (empty response - good case)"""

    def __init__(self, presigned_url, file_path):
        DataHandler.logger(
            'message', translate('CdbsStorageApi', 'Preparing for upload file...')
        )
        self.presigned_url = presigned_url
        self.file_path = file_path
        self.nam = QtNetwork.QNetworkAccessManager(None)
        self.do_request()

    def do_request(self):
        file = QFile(self.file_path.absolute().as_posix())
        if not file.open(QtCore.QIODevice.OpenModeFlag.ReadOnly):
            DataHandler.logger(
                'message', translate('CdbsStorageApi', 'Can not read file...')
            )
            return
        try:
            request = QtNetwork.QNetworkRequest()
            request.setUrl(QtCore.QUrl(self.presigned_url))
            reply = self.nam.put(request, file)
            loop = QtCore.QEventLoop()
            DataHandler.logger('message', translate('CdbsStorageApi', 'Upload file...'))
            reply.finished.connect(loop.quit)
            loop.exec_()
        except Exception as e:
            DataHandler.logger(
                'error',
                translate('CdbsStorageApi', 'Exception in upload file:')
                + f' {e}',
            )
        else:
            response_bytes = DataHandler.handle_response(reply)
            DataHandler.logger(
                'log',
                translate('CdbsStorageApi', 'File uploaded. Response bytes:')
                + f' {response_bytes}',
            )
