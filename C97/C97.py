#name = input("Enter your name:- ")

#word = input("Enter A Word:- ")

#print("No. of characters = ", len(name))

#print("No. of words = ", len(name.split(" ")))

num =input("Enter numbers separated by space - ")

lis = [int(i) for i in num.split(" ")]

lis.sort()
lis.reverse()

print(lis)
