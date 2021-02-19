import dropbox
import os
import shutil

class TransferData:
   def __init__(self, access_token):
       self.access_token = access_token

   def uploadFile(self, source, dest): 
      dbx = dropbox.Dropbox(self.access_token)

      f = open(source, "rb")
      dbx.files_upload(f.read(), dest)

accessToken = "<YOUR ACCESS TOKEN HERE>"
transfer = TransferData(accessToken)

source = input("Path of file to upload:- ")
dest = input("Path to be uploaded to dropbox (along with file name):- ")

os.chdir(source)
lis = os.listdir()

try:
   for i in lis:
       (filename, ext) = os.path.splitext(i)
       if ext =="":
           continue
       else:
          dest = ext
          print("/"+dest.replace(".","")+"/"+filename+dest)
          transfer.uploadFile(i, "/"+dest.replace(".","")+"/"+filename+dest)
except Exception as e:
   print(f"Error Uploading File. Following error occurred:\n{e}")
else:
   print("Upload Successful")
