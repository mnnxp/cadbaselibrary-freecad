""" This file contains one class for register on the CADBase platform """

from pathlib import Path
import CdbsModules.CdbsEvn as CdbsEvn
from CdbsModules.CdbsAuth import CdbsAuth
from CdbsModules.CdbsApi import CdbsApi
from CdbsModules.QueriesApi import QueriesApi
from CdbsModules.DataHandler import deep_parsing_gpl, logger
from CdbsModules.Translate import translate


def register_new_user():
    cdbs_username = CdbsEvn.g_param.GetString('cdbs_username', '')
    cdbs_password = CdbsEvn.g_param.GetString('cdbs_password', '')
    if cdbs_username and cdbs_password:
        CdbsRegUser(cdbs_username, cdbs_password)
        CdbsAuth(cdbs_username, cdbs_password)


class CdbsRegUser:
    """Register a new user the CADBase platform"""

    def __init__(self, username, password):
        logger('debug', translate('cdbs', 'API Point:') + f' {CdbsEvn.g_cdbs_api}')
        logger('message', translate('cdbs', 'New user registration, please wait.'))
        CdbsApi(QueriesApi.register_user(username, password))
        self.fileset_uuid = deep_parsing_gpl('registerUser')
        logger(
            'log',
            translate('cdbs', 'New user UUID:') + f' {self.fileset_uuid}',
        )
