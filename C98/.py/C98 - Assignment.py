def addToFile(file, txt):
    with open(file, "a+") as f:
       for i in txt:
           if i == "":
               continue
           f.writelines(i)

def readFile(file, ret=None):
    with open(file, "r") as f:
        lines = f.readlines()
        print(lines)
        if ret == None:
            for line in lines:
                i = line.replace("\n","")
                print(i)
        else:
            return lines
    
def swapFiles(file1, file2):
   with open(file1, "r+") as f1:
        line1 = f1.readlines()
        with open(file2, "r+") as f2:
            line2 = f2.readlines()
            open(file1, 'w').close()
            f1.writelines(line2)
            open(file2, 'w').close()
            f2.writelines(line1)
            f2.close()
        f1.close()

print("1. Press 1 to append to the file\n2. Press 2 to read the content of files\n3. Press 3 to copy to another file.")

while True:
    choice = int(input("Enter your Choice:- "))


    if choice ==1:
        inpt = input("Enter a text to append (separated by . for multiple lines):- ")
        inpt = inpt.split(".")
        addToFile("test.txt",inpt)
    elif choice == 2:
        inpt = input("Enter Name of file:- ")
        readFile(inpt)
    elif choice ==3:
        file1 = input("Enter Name of 1st File:- ")
        file2 = input("Enter Name of 2nd File:- ")
        swapFiles(file1, file2)
