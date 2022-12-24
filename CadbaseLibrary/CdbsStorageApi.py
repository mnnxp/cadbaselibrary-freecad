''' Functionality for processing requests to the storage of CADBase platform '''

import json
import pathlib
from PySide import QtCore  # FreeCAD's PySide
from PySide2 import QtNetwork
from PySide2.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
import FreeCAD as App
# from CadbaseLibrary.CdbsEvn import g_param, g_content_type, g_response_path
import CadbaseLibrary.DataHandler as DataHandler
# from DataHandler import DataHandler.logger


def parsing_response(reply):
    if DataHandler.handle_response(reply):
        DataHandler.logger('message', f'Upload file success: {reply.response_bytes}')
    else:
        DataHandler.logger('message', f'Upload file success: {reply.response_bytes}')


class CdbsStorageApi:
    ''' class for sending a file to CADBase storarge and handling responses '''

    def __init__(self, presigned_url, file_path):
        DataHandler.logger('message', 'Preparing for upload file...')
        self.presigned_url = presigned_url
        self.file_path = file_path
        self.nam = QNetworkAccessManager(None)
        self.do_request()

    def do_request(self):
        req = QNetworkRequest()
        req.setUrl(QtCore.QUrl(self.presigned_url))
        data = open(self.file_path, 'rb', buffering=0)
        # reply = self.nam.put(req, data=QFile(file_path))
        reply = self.nam.put(req, data)
        loop = QtCore.QEventLoop()
        reply.finished.connect(loop.quit)
        loop.exec_()
        parsing_response(reply)
