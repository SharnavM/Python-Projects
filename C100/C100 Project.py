import random

class ATM(object):
    def __init__(self, cardNum, PIN):
        self.cardnum = cardNum
        self.pin = PIN
        self.balance = random.randrange(5000,50000*2)

    def checkBalance(self):
        print(f"Your Current Balance is {self.balance}")
    
    def withdraw(self, amt):
        if amt> self.balance:
            print("Insufficent Balance")
        else:
            self.balance -= amt
            print(f"Withdrawl successful. Your Current Balance is {self.balance}")

card_num = input("Enter your Card Number:- ")
pin = int(input("Enter your PIN:- "))

user = ATM(card_num, pin)
while True:
    try:
        print("\n1. Check Blance\n2. Withdraw Money")
        choice = int(input("\nEnter Choice:-"))

        if choice == 1:
            user.checkBalance()
        elif choice==2:
            amt = float(input("Enter amt to withdraw:- "))
            user.withdraw(amt)
        else:
            print("Enter Valid Number. \n")
    except:
        print("Bad Input.")
