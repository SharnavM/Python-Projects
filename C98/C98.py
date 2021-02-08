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

def copyToAnother(file1, file2):
    content  = readFile(file1, ret=True)
    swap = [i.swapcase() for i in content]
    addToFile(file2, swap)
    
def copyToAnotherReverse(file1, file2):
    content  = readFile(file1, ret=True)
    arr = [i for i in content]
    rev = []
    for i in arr:
        y = i.replace("\n","")
        y = y.split(" ")
        y.reverse()
        y = " ".join(y)
        y=y+"\n"
        rev.append(y)
    addToFile(file2, rev)

print("1. Press 1 to append to the file\n2. Press 2 to read the content of files\n3. Press 3 to copy to another file.")

while True:
    choice = int(input("Enter your Choice:- "))


    if choice ==1:
        inpt = input("Enter a text to append (separated by . for multiple lines):- ")
        inpt = inpt.split(".")
        addToFile("test.txt",inpt)
    elif choice == 2:
        readFile("test.txt")
    elif choice ==3:
        file1 = input("Enter File to be copied:- ")
        file2 = input("Enter New File:- ")
        copyToAnotherReverse(file1, file2)
