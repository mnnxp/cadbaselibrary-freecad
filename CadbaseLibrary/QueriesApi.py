'''
This file stores GraphQL requests for CADbase platform.
Contains queries for the CADBase (using GraphQL API).
'''

import CadbaseLibrary.CdbsEvn as CdbsEvn


class QueriesApi:
    @staticmethod
    def fav_components():
        return {'query': '''{
                  components (args: {
                    favorite: true
                  }) {
                    uuid
                    name
                    ownerUser {
                      uuid
                      username
                    }
                    imageFile {
                      uuid
                      filename
                      downloadUrl
                    }
                  }
                }'''}

    def component_modifications(self, object_uuid):
        return {'query': f'''{{
                  componentModifications (args: {{
                    componentUuid: "{object_uuid}"
                  }}) {{
                    uuid
                    modificationName
                  }}
                }}'''}

    def target_fileset(self, object_uuid):
        return {'query': f'''{{
                  componentModificationFilesets (args: {{
                    modificationUuid: "{object_uuid}"
                    programIds: {CdbsEvn.g_program_id}
                  }}) {{
                    uuid
                  }}
                }}'''}

    def fileset_files(self, object_uuid):
        return {'query': f'''{{
                  componentModificationFilesetFiles (args: {{
                    filesetUuid: "{object_uuid}"
                  }}) {{
                    uuid
                    hash
                    filename
                    downloadUrl
                  }}
                }}'''}

    def register_modification_fileset(self, modification_uuid):
        return {'mutation': f'''{{
                  registerModificationFileset (args: {{
                    modificationUuid: "{modification_uuid}"
                    programId: {CdbsEvn.g_program_id}
                  }})
                }}'''}

    def upload_files_to_fileset(self, fileset_uuid, filenames):
        return {'mutation': f'''{{
                  uploadFilesToFileset (args: {{
                    filesetUuid: "{fileset_uuid}"
                    filenames: {filenames}
                  }}) {{
                    fileUuid
                    filename
                    uploadUrl
                  }}
                }}'''}

    def upload_completed(self, file_uuids):
        return {'mutation': f'''{{
                  uploadCompleted (args: {{
                    fileUuids: "{file_uuids}"
                  }})
                }}'''}

    def delete_files_from_fileset(self, fileset_uuid, file_uuids):
        return {'mutation': f'''{{
                  deleteFilesFromFileset (args: {{
                    filesetUuid: "{fileset_uuid}"
                    fileUuids: "{file_uuids}"
                  }})
                }}'''}
