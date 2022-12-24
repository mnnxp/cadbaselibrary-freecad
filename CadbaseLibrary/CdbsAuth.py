''' This file contains one class for authorization on the CADBase platform '''

import json
from PySide import QtCore  # FreeCAD's PySide
from PySide2 import QtNetwork
# import FreeCAD as App
# from CdbsEvn import g_param, g_api_login, g_content_type
import CadbaseLibrary.CdbsEvn as CdbsEvn
import CadbaseLibrary.DataHandler as DataHandler
# from DataHandler import DataHandler.logger


def parsing_response(reply):
    response_bytes = DataHandler.handle_response(reply)
    if response_bytes:
        token = json.loads(str(response_bytes, 'utf-8'))
        CdbsEvn.g_param.SetString('auth-token', token['bearer'])

        DataHandler.logger('message', 'Successful authorization')
    else:
        DataHandler.logger('error', 'Failed authorization')


class CdbsAuth:
    ''' class for getting a token to access the CADBase platform '''

    def __init__(self, username, password):
        DataHandler.logger('message', 'Getting a new token, please wait.')
        query = {'user': {'username': username, 'password': password}}
        self.nam = QtNetwork.QNetworkAccessManager(None)
        self.do_request(query)

    def do_request(self, query):
        req = QtNetwork.QNetworkRequest()
        req.setUrl(QtCore.QUrl(CdbsEvn.g_api_login))
        req.setRawHeader(b'Content-Type', CdbsEvn.g_content_type)
        body = json.dumps(query).encode('utf-8')
        reply = self.nam.post(req, body)
        loop = QtCore.QEventLoop()
        reply.finished.connect(loop.quit)
        loop.exec_()
        parsing_response(reply)
