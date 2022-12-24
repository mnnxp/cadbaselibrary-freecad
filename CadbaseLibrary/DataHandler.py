''' Here are functions for working with data (links, storage, files) '''

import os
import time
import json
import pathlib
from types import SimpleNamespace
from multiprocessing import cpu_count
from multiprocessing.pool import ThreadPool
from PySide import QtCore  # FreeCAD's PySide
from PySide2 import QtNetwork
import FreeCAD as App
import CadbaseLibrary.CdbsEvn as CdbsEvn


def logger(type_msg, msg):
    if type_msg == 'error':
        App.Console.PrintError(f'{msg}\n')
    elif type_msg == 'warning':
        App.Console.PrintWarning(f'{msg}\n')
    elif type_msg == 'message':
        App.Console.PrintMessage(f'{msg}\n')
    else:
        App.Console.PrintLog(f'{msg}\n')


def handle_response(reply):
    er = reply.error()
    if er == QtNetwork.QNetworkReply.NoError:
        if reply.attribute(QtNetwork.QNetworkRequest.HttpStatusCodeAttribute) == 200:
            logger('message', 'Success')
            return reply.readAll()
        else:
            logger('error',
                   f'Failed, status code: {reply.attribute(QtNetwork.QNetworkRequest.HttpStatusCodeAttribute)}')
    else:
        logger('error', f'Error occurred: {er}')
        logger('error', f'{reply.errorString()}')


def validation_uuid(check_uuid):
    # used for check valid uuid
    return len(check_uuid) == 36


def get_file(args):
    '''
    This function downloads and saves a file of args data to the user's local storage.
    Argument (args) for this function have a url and filepath (path/filename).
    '''
    t0 = time.time()
    url = args[0]
    filepath = args[1]
    if filepath.exists():
        logger('warning', f'File "{filepath}" already exists and skipped.')
        return filepath, time.time() - t0
    manager = QtNetwork.QNetworkAccessManager(None)
    try:
        request = QtNetwork.QNetworkRequest()
        request.setUrl(QtCore.QUrl(url))
        request.setRawHeader(b'User-Agent', CdbsEvn.g_user_agent)
        reply = manager.get(request)
        loop = QtCore.QEventLoop()
        reply.finished.connect(loop.quit)
        loop.exec_()
    except Exception as e:
        logger('error', f'Exception in download file: {e}')
    else:
        if reply.error() == QtNetwork.QNetworkReply.NoError:
            response_bytes = reply.readAll()
            with filepath.open('wb') as f:
                f.write(response_bytes)
            return filepath, time.time() - t0
        else:
            logger('error', 'Error')


def download_parallel(args):
    t0 = time.time()
    results = ThreadPool(cpu_count() - 1).imap_unordered(get_file, args)
    for result in results:
        logger('log', f'path: "{result[0]}" time: {result[1]} s')
    logger('message', f'Total time: {time.time() - t0} s')


def parsing_gpl():
    logger('message', 'Data processing, please wait.')
    if CdbsEvn.g_response_path.exists():
        temp = CdbsEvn.g_response_path.open('r', encoding='UTF-8').readline()
        logger('log', f'Response data: {temp}')
        # get only first line if expecting uuid or boolean value
        # if validation_uuid(CdbsEvn.g_response_path) or len(CdbsEvn.g_response_path) < 7:
        #     # get first line from file with response
        #     return CdbsEvn.g_response_path.open('r', encoding='UTF-8').readline()
        with CdbsEvn.g_response_path.open('rb', buffering=0) as f:
            res = json.loads(f.readall(),
                             object_hook=lambda d: SimpleNamespace(**d))
        if res.data:
            return res.data
        else:
            logger('error', 'Error occured:')
            for error in res.errors:
                logger('error', error.message)
    else:
        logger('error', 'No file with response')

    logger('error', 'Failed')


def remove_object(rm_object: pathlib.Path):
    ''' delete directory or file from local storage '''
    if rm_object.exists():
        if rm_object.is_dir():
            os.rmdir(rm_object)
        else:
            os.remove(rm_object)
        logger('log', f'"{rm_object}" removed')


def create_object_path(new_dir: pathlib.Path, object_info: str, object_type: str):
    ''' create a new object path '''
    if new_dir.exists() and not new_dir.is_dir():
        logger('error', f'Please remove the "{new_dir}" file for correct operation')
    else:
        if not new_dir.is_dir():
            os.mkdir(new_dir)
        new_info_file = new_dir / object_type
        try:
            with new_info_file.open('w') as f:
                f.write(json.dumps(object_info, default=lambda o: o.__dict__, indent=4))
                f.close()
        except Exception as e:
            logger('error', str(e))


def read_object_info(info_file: pathlib.Path, select_object: str):
    ''' read information about an object from a file '''
    with info_file.open('r') as data_file:
        object_info = json.loads(data_file.read(),
                                 object_hook=lambda d: SimpleNamespace(**d))
        logger('log', f'Select {select_object}: {object_info.uuid}')
        data_file.close()
        return object_info


