class BankAccount(object):
    def __init__(self, name, num,balance,typeof, branch):
        self.name = name
        self.num = num
        self.typeof = typeof
        self.branch = branch
        self.balance = balance

    def withdraw(self, amt):
        if amt < 0:
            print("Enter Proper Amount.")
        elif self.balance < amt:
            print("Not enough Balance to withdraw.\n")
        else:
            self.balance -= amt
            print(f"Withdraw Successful. Your current balance is {self.balance}\n")


    def deposit(self, amt):
        if amt < 0:
            print("Enter Proper Amount.")
        else:
            self.balance += amt
            print(f"Deposit Successful. Your current balance is {self.balance}")

    def loan(self):
        amt = float(input("Enter Amount:- "))
        time = float(input("Enter Time (in year):- "))
        rate = float(input("Enter Rate (in %)- "))

        principal_amt = self.calculateInterest(amt,time,rate)
        print(f"Total Payable Amount at end is {principal_amt}")

        confirm = input("Sanction This Loan (Y/n)? ")

        if confirm.lower() == "y":
            self.balance += amt
            print("Loan Sanctioned Successfully")

    def calculateInterest(self, amt, time, rate):
        interest = amt*time*rate/100
        final_amt = amt + interest
        print(f"Interest payable is {interest}")
        return final_amt
        

user1 = BankAccount("User1", 12, 5000, "Savings","Pune")
user2 = BankAccount("User2", 40, 50000, "Savings","Pune")
user3 = BankAccount("User3", 76, 15000, "Savings","Pune")

lis = [user1, user2, user3]

while True:
    user = int(input("Enter Account Number: - "))
    for i in lis:
        if i.num == user:
            user = i
            break
    else:
        user = None
        print("Account Doesn't Exist\n")
    if user is not None:
        print("1. Press 1 to Withdraw Money\n2. Press 2 to Deposit Money\n 3. Sanction Loan")
        choice = int(input("Enter Choice:- "))
        if choice == 1:
            mon = int(input("Enter Amount to withdraw:- "))
            user.withdraw(mon)
        elif choice == 2:
            mon = int(input("Enter Amount to Deposit:- "))
            user.deposit(mon)
        elif choice == 3:
            user.loan()
