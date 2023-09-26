""" This file contains one class for authorization on the CADBase platform """

import json
from PySide import QtCore, QtNetwork  # FreeCAD's PySide
import CdbsModules.CdbsEvn as CdbsEvn
import CdbsModules.DataHandler as DataHandler
from CdbsModules.Translate import translate


def parsing_response(reply):
    response_bytes = DataHandler.handle_response(reply)
    if response_bytes:
        token = json.loads(str(response_bytes, 'utf-8'))
        CdbsEvn.g_param.SetString('auth-token', token['bearer'])
        DataHandler.logger('message', translate('CdbsAuth', 'Successful authorization'))
    else:
        DataHandler.logger('error', translate('CdbsAuth', 'Failed authorization'))


class CdbsAuth:
    """Getting a token to access the CADBase platform"""

    def __init__(self, username, password):
        DataHandler.logger(
            'message',
            translate('CdbsAuth', 'Getting a new token, please wait.'),
        )
        self.query = {'user': {'username': username, 'password': password}}
        self.nam = QtNetwork.QNetworkAccessManager(None)
        self.do_request()

    def do_request(self):
        try:
            request = QtNetwork.QNetworkRequest()
            request.setUrl(QtCore.QUrl(CdbsEvn.g_api_login))
            request.setRawHeader(b'Content-Type', CdbsEvn.g_content_type)
            body = json.dumps(self.query).encode('utf-8')
            reply = self.nam.post(request, body)
            loop = QtCore.QEventLoop()
            reply.finished.connect(loop.quit)
            loop.exec_()
            # deleting references to an object with confidential data
            del body
            del self.query
        except Exception as e:
            DataHandler.logger(
                'error',
                translate('CdbsAuth', 'Exception when trying to login:')
                + f' {e}',
            )
        else:
            parsing_response(reply)
