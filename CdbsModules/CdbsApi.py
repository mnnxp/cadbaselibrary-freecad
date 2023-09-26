""" Functionality for processing requests to the CADBase platform """

import json
from PySide import QtCore, QtNetwork  # FreeCAD's PySide
import CdbsModules.CdbsEvn as CdbsEvn
import CdbsModules.DataHandler as DataHandler
from CdbsModules.Translate import translate


def parsing_response(reply):
    response_bytes = DataHandler.handle_response(reply)
    if response_bytes:
        DataHandler.remove_object(CdbsEvn.g_response_path)  # deleting old a response if it exists
        with CdbsEvn.g_response_path.open('wb') as file:
            file.write(response_bytes)
        DataHandler.logger('message', translate('CdbsApi', 'Successful processing request'))
    else:
        DataHandler.logger('error', translate('CdbsApi', 'Failed processing request'))


class CdbsApi:
    """Sending a request to the CADBase API and processing the response"""

    def __init__(self, query):
        DataHandler.logger('message', translate('CdbsApi', 'Getting data...'))
        self.nam = QtNetwork.QNetworkAccessManager(None)
        self.do_request(query)

    def do_request(self, query):
        try:
            request = QtNetwork.QNetworkRequest()
            request.setUrl(QtCore.QUrl(CdbsEvn.g_cdbs_api))
            auth_header = 'Bearer ' + CdbsEvn.g_param.GetString('auth-token', '')
            request.setRawHeader(b'Content-Type', CdbsEvn.g_content_type)
            request.setRawHeader(b'Authorization', auth_header.encode())
            body = json.dumps(query).encode('utf-8')
            DataHandler.logger(
                'log', translate('CdbsApi', 'Query include body:') + f' {body}'
            )
            reply = self.nam.post(request, body)
            loop = QtCore.QEventLoop()
            reply.finished.connect(loop.quit)
            loop.exec_()
        except Exception as e:
            DataHandler.logger(
                'error',
                translate('CdbsApi', 'Exception when trying to sending the request:')
                + f' {e}'),
        else:
            parsing_response(reply)
