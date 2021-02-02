import random

count = 0

randInt = random.randint(1,9)

while count<5:
    try:
        inpt = int(input("Enter a number (1-9) :- "))
    except:
        print("Input an integer next time\n")
        break

    count +=1
  

    if inpt < randInt:
        print(f"Your Guess was low. Enter a number greater than {inpt} next time\n")
    elif inpt>randInt:
        print(f"Your Guess was high. Enter a number lesser than {inpt} next time\n")
    else:
        print("Congratulations!! You Won\n")
        break

print("Your chances are over. You Lose!!!")
