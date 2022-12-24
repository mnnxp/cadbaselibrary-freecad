''' Functionality for processing requests to the CADBase platform '''

import json
import pathlib
from PySide import QtCore  # FreeCAD's PySide
from PySide2 import QtNetwork
import FreeCAD as App
import CadbaseLibrary.CdbsEvn as CdbsEvn
import CadbaseLibrary.DataHandler as DataHandler
# from DataHandler import DataHandler.logger


def parsing_response(reply):
    response_bytes = DataHandler.handle_response(reply)
    if response_bytes:
        DataHandler.remove_object(CdbsEvn.g_response_path)  # deleting old a response if it exists
        with CdbsEvn.g_response_path.open('wb') as file:
            file.write(response_bytes)
        DataHandler.logger('message', 'Successful processing request')
    else:
        DataHandler.logger('error', 'Failed processing request')


class CdbsApi:
    ''' class for sending requests and handling responses '''

    def __init__(self, query):
        # DataHandler.logger('message', 'Getting data...')
        DataHandler.logger('warning', f'Query data: {query}')
        self.nam = QtNetwork.QNetworkAccessManager(None)
        self.do_request(query)

    def do_request(self, query):
        api_url = CdbsEvn.g_param.GetString('api-url', '')
        req = QtNetwork.QNetworkRequest()
        req.setUrl(QtCore.QUrl(api_url))
        auth_header = 'Bearer ' + CdbsEvn.g_param.GetString('auth-token', '')
        header = {'Authorization': auth_header}
        req.setRawHeader(b'Content-Type', CdbsEvn.g_content_type)
        req.setRawHeader(b'Authorization', auth_header.encode())
        body = json.dumps(query).encode('utf-8')
        reply = self.nam.post(req, body)
        loop = QtCore.QEventLoop()
        reply.finished.connect(loop.quit)
        loop.exec_()
        parsing_response(reply)
