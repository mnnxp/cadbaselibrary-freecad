"""This file stores GraphQL requests for CADbase platform.
Contains queries for the CADBase (using GraphQL API).
"""

import json
import CdbsModules.CdbsEvn as CdbsEvn


class QueriesApi:
    def register_user(username: str, password: str):
        return dict(
          query=f'''mutation {{
              registerUser (args: {{
                email: ""
                username: "{username}"
                password: "{password}"
                programId: 42
              }}) {{
                uuid
              }}
            }}'''
        )

    @staticmethod
    def fav_components():
        return dict(
          query='''query {
              components (args: {
                favorite: true
              }) {
                uuid
                name
                ownerUser {
                  uuid
                  username
                }
              }
            }'''
        )

    def component_modifications(object_uuid: str):
        return dict(
          query=f'''query {{
              componentModifications (componentUuid: "{object_uuid}") {{
                uuid
                modificationName
              }}
            }}'''
        )

    def target_fileset(object_uuid: str):
        return dict(
          query=f'''query {{
              componentModificationFilesets (args: {{
                modificationUuid: "{object_uuid}"
                programIds: {CdbsEvn.g_program_id}
              }}) {{
                uuid
              }}
            }}'''
        )

    def fileset_files(object_uuid):
        return dict(
          query=f'''query {{
              componentModificationFilesOfFileset (
                args: {{ filesetUuid: "{object_uuid}" }}
                paginate: {{
                  currentPage: 1
                  perPage: 1000
                  }}
              ) {{
                uuid
                sha256Hash
                filename
                filesize
                updatedAt
                downloadUrl
              }}
            }}'''
        )

    def register_component(component_name, component_description):
        return dict(
          query=f'''mutation {{
                registerComponent (args: {{
                    name: "{component_name}"
                    description: "{component_description}"
                    typeAccessId: 1
                    componentTypeId: 1
                    actualStatusId: 1
                    isBase: false
                }})
            }}'''
        )

    def register_modification_fileset(modification_uuid):
        return dict(
          query=f'''mutation {{
                registerModificationFileset (args: {{
                    modificationUuid: "{modification_uuid}"
                    programId: {CdbsEvn.g_program_id}
                }})
            }}'''
        )

    def upload_files_to_fileset(fileset_uuid, filenames, commit_msg):
        fix_commit_msg = commit_msg.replace('\\','\\\\').replace('\"','\\\"')
        return dict(
          query=f'''mutation {{
              uploadFilesToFileset (args: {{
                filesetUuid: "{fileset_uuid}"
                filenames: {json.dumps(filenames)}
                commitMsg: "{fix_commit_msg}"
              }}) {{
                fileUuid
                filename
                uploadUrl
              }}
            }}'''
        )

    def upload_completed(file_uuids: list):
        return dict(
          query=f'''mutation {{
              uploadCompleted (fileUuids: {json.dumps(file_uuids)})
            }}'''
        )

    def delete_files_from_fileset(fileset_uuid, file_uuids: list):
        return dict(
          query=f'''mutation {{
              deleteFilesFromFileset (args: {{
                filesetUuid: "{fileset_uuid}"
                fileUuids: {json.dumps(file_uuids)}
              }})
            }}'''
        )
