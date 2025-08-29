"""Global variables of the macro are collected here"""

import pathlib
from PySide.QtGui import QFileDialog, QApplication  # FreeCAD's PySide
import FreeCAD as app


g_param = app.ParamGet('User parameter:Plugins/cadbase_library')
g_base_api = 'https://api.cadbase.rs'  # default CADBase platform point
g_api_login = f'{g_base_api}/login'
g_cdbs_api = f'{g_base_api}/graphql'
g_program_id = 42  # this is FreeCAD ID in CADBase
g_program_name = 'FreeCAD'
g_user_agent = b'Mozilla/5.0 (Macintosh; Intel Mac OS 10 12.3; rv:42.0) \
                Gecko/20100101 Firefox/42.0'
g_content_type = b'application/json'
g_ui_file = (
    app.getUserAppDataDir()
    + 'Mod/CadbaseLibrary/CdbsModules/cadbase_library.ui'
)
g_ui_file_upload = (
    app.getUserAppDataDir()
    + 'Mod/CadbaseLibrary/CdbsModules/cadbase_library_upload.ui'
)
g_ui_file_config = (
    app.getUserAppDataDir()
    + 'Mod/CadbaseLibrary/CdbsModules/cadbase_library_config.ui'
)
g_ui_file_token = (
    app.getUserAppDataDir()
    + 'Mod/CadbaseLibrary/CdbsModules/cadbase_library_token.ui'
)
g_ui_file_component = (
    app.getUserAppDataDir()
    + 'Mod/CadbaseLibrary/CdbsModules/cadbase_library_object.ui'
)
g_len_uuid = 36  # for a little uuid validation
# for save the path to the local CADBase library
g_library_path = g_param.GetString('destination')
# flag for re-authorization in case of token expiration
g_relogin_flag = False


def set_library_path():
    """Getting the location for the CADBase library,
    if the value is empty or invalid, the existing location is requested from the user
    """
    global g_library_path
    destination = g_param.GetString('destination')
    if destination and pathlib.Path(destination).is_dir():
        return destination
    new_destination = QFileDialog.getExistingDirectory(
        None,
        QApplication.translate(
            'CADBaseLibrary', 'Location of your existing CADBase library'
        ),
    )
    # forward slashes apparently work on windows too
    g_param.SetString('destination', new_destination.replace('\\', '/'))
    g_library_path = g_param.GetString('destination')
    return g_library_path


def set_base_param():
    """Setting default options if they weren't set before"""
    if not g_param.GetString('api-url'):
        g_param.SetString('api-url', g_base_api)
    if not g_param.GetString('auth-token'):
        g_param.SetString('auth-token', '')
    if not g_param.GetString('skip-hash'):
        g_param.SetString('skip-hash', '')  # False is '' and True is 'True'
    if not g_param.GetString('force-upload'):
        g_param.SetString('force-upload', '')  # False is '' and True is 'True'


def update_api_points():
    """Updating API points, it's need in case the root point changes"""
    global g_api_login
    global g_cdbs_api
    root_api = g_param.GetString('api-url')
    if not root_api:
        root_api = g_base_api
    g_api_login = f'{root_api}/login'
    g_cdbs_api = f'{root_api}/graphql'


set_library_path()  # update library path
update_api_points()  # update api points
# Please don't use this name as the name of files or folders in the CADBase Library folder.
g_response_path = pathlib.Path(g_library_path) / 'cadbase_file_2018'
g_log_file_path = g_response_path.with_suffix('.log')
