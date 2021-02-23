import os
import dropbox
from dropbox.files import WriteMode

class TransferFile(object):
    def __init__(self, access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for file in files:
                local_path = os.path.join(root, file)
                rel_path = os.path.relpath(local_path, file_from)
                dbx_path = os.path.join(file_to, rel_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dbx_path, mode=WriteMode('overwrite'))

accessToken = "<access-token>"
transferFile = TransferFile(access_token)

src = input("Enter the folder path to transfer : -")
dest = input("Enter the full path to upload to dropbox:- ")

transferFile.upload_file(src, dest)
print("Operation Completed.")
