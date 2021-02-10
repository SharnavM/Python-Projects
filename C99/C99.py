import os
import shutil
#os.system("date")

#os.mkdir(r".\Test")

#print(os.getcwd())

#print(os.path.exists(r".\Test"))

'''(filename, ext) = os.path.splitext(r".\C99.py")
print(filename)
print(ext)'''

os.chdir(r"A:\WhiteHatJr\Python")

#print(os.listdir())

#shutil.move(r"A:\WhiteHatJr\Python\Test",r"A:\WhiteHatJr\Python\C99\Test")

def copy(src, dest):
    shutil.copytree(src, dest)

src = input("Enter source path:- ")
dest = input("Enter destination path:- ")

os.chdir(src)

lis = os.listdir()
print(lis)

copy(src, dest)

