"""Functionality for processing requests to the storage of CADBase platform"""

import time
from pathlib import Path
from multiprocessing import cpu_count
from multiprocessing.pool import ThreadPool
from CdbsModules.CdbsApi import CdbsApi
from CdbsModules.CdbsStorageApi import CdbsStorageApi
from CdbsModules.QueriesApi import QueriesApi
import CdbsModules.DataHandler as DataHandler
from CdbsModules.Translate import translate


class CdbsStorage:
    """The class functions determine which files are suitable for uploading to the CADBase storage,
    request data for uploading files, and call functions to upload files to storage.
    """

    def __init__(self, arg):
        """Validation the modification uuid and creating variables for next parsing data"""
        DataHandler.logger(
            'message',
            translate('CdbsStorage', 'Preparing for uploading files...'),
        )
        self.modification_uuid = arg[0]
        self.last_clicked_dir = arg[1]  # set directory from which files will be pushed
        self.commit_msg = ''  # change comment has length limit of 225
        if not Path.is_dir(self.last_clicked_dir):
            DataHandler.logger(
                'warning',
                translate(
                    'CdbsStorage',
                    'To upload files, you must select a modification folder or a set of files',
                ),
            )
            return
        DataHandler.logger(
            'log',
            translate('CdbsStorage', 'Modification UUID:')
            + f' {self.modification_uuid}',
        )
        if not DataHandler.validation_uuid(self.modification_uuid):
            DataHandler.logger(
                'warning',
                translate(
                    'CdbsStorage',
                    'To upload files, you must select a modification \
(set of files for FreeCAD will be selected) or a set of files',
                ),
            )
            return
        self.upload_filenames = []  # filenames for upload to the CADBase storage
        self.delete_file_uuids = []  # uuids of old files on the CADBase storage
        self.affected_files = [] #  preparing data to be displayed in table for user
        self.completed_files = []  # uuid of successfully uploaded files
        self.fileset_uuid = None
        self.new_fileset = False

    def processing_manager(self):
        """Defines a uuid for a set of files and calls functions
        to determine the type of changes before sending the update to CADBase platform
        """
        DataHandler.logger('log', translate('CdbsStorage', 'Getting fileset UUID...'))
        # getting the uuid of a set of files for FreeCAD
        CdbsApi(QueriesApi.target_fileset(self.modification_uuid))
        self.fileset_uuid = DataHandler.get_uuid(
            DataHandler.deep_parsing_gpl('componentModificationFilesets', True)
        )
        DataHandler.logger(
            'log',
            translate('CdbsStorage', 'Fileset UUID:')
            + f' {self.fileset_uuid}',
        )
        if not self.fileset_uuid:
            DataHandler.logger(
                'log',
                translate('CdbsStorage', 'Creating a new set of files for FreeCAD'),
            )
            CdbsApi(QueriesApi.register_modification_fileset(self.modification_uuid))
            self.fileset_uuid = DataHandler.deep_parsing_gpl('registerModificationFileset')
            self.new_fileset = True
        if not DataHandler.validation_uuid(self.fileset_uuid):
            DataHandler.logger(
                'warning',
                translate(
                    'CdbsStorage',
                    'Error occurred while getting the UUID of the file set',
                ),
            )
            return
        if self.fileset_uuid:
            self.define_files()
        return self.affected_files

    def processing_update(self, commit_msg):
        """Sending files to remote storage, confirming successful file upload.
        And deleting from remote storage files that have already been deleted locally.
        """
        self.delete_old_files()  # deleting files from storage that do not exist locally
        self.commit_msg = commit_msg  # change comment has length limit of 225
        if self.upload_filenames:
            # trying to upload files and save a count of successful uploads
            count_up_files = self.upload()
            if not count_up_files:
                DataHandler.logger(
                    'warning',
                    translate(
                        'CdbsStorage',
                        'Error occurred while confirming the upload of files, \
the files were not uploaded to correctly',
                    ),
                )
                return
        else:
            DataHandler.logger('warning', translate('CdbsStorage', 'No files found for upload'))
            return
        if count_up_files > 0:
            DataHandler.logger(
                'message',
                translate(
                    'CdbsStorage',
                    'Success upload files to CADBase storage:',
                )
                + f' {count_up_files}',
            )
        # clear data that will no longer be used
        self.upload_filenames.clear()
        self.delete_file_uuids.clear()
        self.completed_files.clear()
        DataHandler.logger(
            'message',
            translate(
                'CdbsStorage',
                'Files in the CADBase storage have been updated successfully',
            ),
        )

    def define_files(self):
        """Determine files to upload to CADBase storage: getting files from local and remote storage,
        identify duplicates and compare hashes
        """
        local_filenames = []  # files from local storage
        # files from the local storage that are not in the CADBase storage
        DataHandler.logger(
            'log',
            translate('CdbsStorage', 'Last clicked dir:')
            + f' {self.last_clicked_dir}',
        )
        for path in Path.iterdir(self.last_clicked_dir):
            # check if current path is a file and skip if the file with technical information
            if path.is_file() and path.name != 'modification':
                local_filenames.append(path.name)
        DataHandler.logger(
            'log',
            translate('CdbsStorage', 'Local files:')
            + f' {local_filenames}',
        )
        if not local_filenames:
            return  # no potential files for uploads found
        cloud_files = []  # files from CADBase storage
        cloud_filenames = []  # filenames of CADBase storage files
        if not self.new_fileset:
            # get file list with hash from CADBase storage
            CdbsApi(QueriesApi.fileset_files(self.fileset_uuid))
            cloud_files = DataHandler.deep_parsing_gpl('componentModificationFilesetFiles', True)
        for cf in cloud_files:
            cloud_filenames.append(cf.get('filename'))  # selecting cloud filenames for validation with locale files
        DataHandler.logger(
            'log',
            translate('CdbsStorage', 'Cloud filenames:')
            + f' {cloud_filenames}',
        )
        dup_files = []  # files which are in the local and CADBase storage
        for l_filename in local_filenames:
            if not self.new_fileset and l_filename in cloud_filenames:
                DataHandler.logger(
                    'log',
                    translate('CdbsStorage', 'The local file has a cloud version:')
                    + f' "{l_filename}"',
                )
                # save the name of the (old) file for hash check
                dup_files.append(l_filename)
            else:
                DataHandler.logger(
                    'log',
                    translate('CdbsStorage', 'Local file does not have a cloud version:')
                    + f' "{l_filename}"',
                )
                # save the name of the new file to upload
                self.upload_filenames.append(l_filename)
                self.affected_files.append([l_filename, 'new'])
        DataHandler.logger(
            'message',
            translate('CdbsStorage', 'New files to upload:')
            + f' {self.upload_filenames}',
        )
        self.parsing_duplicate(dup_files, cloud_files)
        # comparing file names of local and remote storage to detect deleted files
        for cf in cloud_files:
            if cf.get('filename') not in local_filenames:
                self.delete_file_uuids.append(cf.get('uuid'))
                self.affected_files.append([cf.get('filename'), 'deleted'])
        DataHandler.logger(
            'log',
            translate('CdbsStorage', 'Files for deletion:')
            + f' {self.delete_file_uuids}',
        )

    def parsing_duplicate(self, dup_files, cloud_files):
        """Compare hash for local and CADBase storage files, add files for update if hash don't equally"""
        try:
            from blake3 import blake3
        except Exception as e:
            DataHandler.logger(
                'error',
                translate('CdbsStorage', 'Blake3 import error:')
                + f' {e}',
            )
            DataHandler.logger(
                'warning',
                translate(
                    'CdbsStorage',
                    'Warning: for compare hashes need install `blake3`. \
Please try to install it with: `pip install blake3` or some other way.',
                ),
            )
            return
        for df in dup_files:
            cloud_file = next(item for item in cloud_files if item['filename'] == df)
            if not cloud_file['hash']:
                DataHandler.logger(
                    'warning',
                    translate(
                        'CdbsStorage',
                        'File hash from CADBase not found, this file is skipped:',
                    )
                    + f' "{df}"',
                )
                continue
            local_file_path = Path(self.last_clicked_dir) / df
            if not local_file_path.is_file():
                DataHandler.logger(
                    'warning',
                    translate(
                        'CdbsStorage',
                        'Warning: found not file and it skipped',
                    )
                    + f' ("{df}")',
                )
                break
            try:
                file = local_file_path.open('rb', buffering=0)
                local_file_hash = blake3(file.read()).hexdigest()
                file.close()
            except Exception as e:
                DataHandler.logger(
                    'error',
                    translate('CdbsStorage', 'Error calculating hash for local file')
                    + f' {local_file_hash}: {e}',
                )
                break
            DataHandler.logger(
                'log',
                translate('CdbsStorage', 'Hash file')
                + f' {df}:\n{local_file_hash} ('
                + translate('CdbsStorage', 'local')
                + f')\n{cloud_file["hash"]} ('
                + translate('CdbsStorage', 'cloud')
                + ')',
            )
            # check the hash if it exists for both files
            if (
                local_file_hash
                and cloud_file['hash']
                and local_file_hash != cloud_file['hash']
            ):
                self.upload_filenames.append(df)
                self.affected_files.append([df, 'updated'])

    def upload(self):
        """Getting information (file IDs, pre-signed URLs) to upload files to CADBase storage
        and calling the function to upload files in parallel
        """
        DataHandler.logger(
            'message',
            translate('CdbsStorage', 'Selected files to upload:')
            + f' {self.upload_filenames}',
        )
        CdbsApi(QueriesApi.upload_files_to_fileset(self.fileset_uuid, self.upload_filenames, self.commit_msg))
        # data for uploading by each file
        args = DataHandler.deep_parsing_gpl('uploadFilesToFileset', True)
        if not args:
            return 0
        # data for uploading files to storage received
        DataHandler.logger(
            'message',
            translate(
                'CdbsStorage',
                'Uploading files to cloud storage (this can take a long time)',
            ),
        )
        self.upload_parallel(args)
        if not self.completed_files:
            DataHandler.logger(
                'log',
                translate('CdbsStorage', 'Failed to upload files'),
            )
            return 0
        # at least some files were uploaded successfully
        CdbsApi(QueriesApi.upload_completed(self.completed_files))
        res = DataHandler.deep_parsing_gpl('uploadCompleted')
        DataHandler.logger(
            'log',
            translate('CdbsStorage', 'Confirmation of successful files upload:')
            + f' {res}',
        )
        return res

    def put_file(self, arg: dict):
        """Uploading a file via presigned URL to the CADBase storage"""
        t0 = time.time()
        filename = arg.get('filename')
        file_path = self.last_clicked_dir / filename
        if CdbsStorageApi(arg.get('uploadUrl'), file_path):
            DataHandler.logger(
                'log',
                translate('CdbsStorage', 'Completed upload:')
                + f' "{filename}"',
            )
            self.completed_files.append(arg.get('fileUuid'))
        return filename, time.time() - t0

    def upload_parallel(self, args: list):
        """Asynchronous calling of the function of uploading files to the CADBase storage
        in several threads (if available)
        """
        t0 = time.time()
        results = ThreadPool(cpu_count() - 1).imap_unordered(self.put_file, args)
        for result in results:
            DataHandler.logger(
                'log',
                translate('CdbsStorage', 'Filename:')
                + f' "{result[0]}"'
                + translate('CdbsStorage', 'time:')
                + f' {result[1]} '
                + translate('CdbsStorage', 'sec'),
            )
        DataHandler.logger(
            'message',
            translate('CdbsStorage', 'Total time:')
            + f'{time.time() - t0}'
            + translate('CdbsStorage', 'sec'),
        )

    def delete_old_files(self):
        """Deleting obsolete files from CADBase storage"""
        if self.delete_file_uuids:
            CdbsApi(QueriesApi.delete_files_from_fileset(self.fileset_uuid, self.delete_file_uuids))
            res = DataHandler.deep_parsing_gpl('deleteFilesFromFileset')
            DataHandler.logger('log', f'Delete files from fileset: {res}')
            return res
        return False
