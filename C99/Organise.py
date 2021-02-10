import os
import shutil

src= input("Enter path of directory to organise:- ")

os.chdir(src)
lis = os.listdir()

for i in lis:
    (filename, ext) = os.path.splitext(i)
    if ext =="":
        continue
    else:
        if os.path.exists(ext):
            shutil.move(i, src+"\\"+ext+"\\")
        else:
            os.mkdir(ext)
            shutil.move(i, src+"\\"+ext+"\\")
            
