from random import randint


class Account:
    balance = (randint(1000, 20000))

    def __init__(self, Name, Ac, Ac_type):
        self.name = Name
        self.ac = Ac
        self.type = Ac_type

    def deposit(self, Amount):
        print("Successfully Deposited")
        self.balance += Amount

    def withdraw(self, Amount):
        print("Withdrawal Successful")
        self.balance -= Amount


class FixDeposit(Account):
    fd_rate = 6.4

    def __init__(self, Fd_amt):
        super().__init__(name, ac, Type)
        self.fd_amt = Fd_amt

    def cal_fd(self):
        si = (self.fd_amt * self.fd_rate * 10) / 100
        print("Final Amount After 10 years is : ", si + self.fd_amt)

    def display_fd(self):
        print("---------------------------------------")
        print("Name : ", self.name)
        print("A/c No. :- ", self.ac)
        print("A/c Type: ", self.type)
        print("Balance: ", self.balance)
        print("FD Amount: ", self.fd_amt)
        print("Fix Deposit Successfully Created......")


class Loan(Account):
    loan_rate = 8.5

    def __init__(self, Loan_amt):
        super().__init__(name, ac, Type)
        self.loan_amt = Loan_amt

    def cal_loan(self):
        si = (self.loan_amt * self.loan_rate * 10) / 100
        print("Final Amount After 10 years is : ", si + self.loan_amt)

    def display_loan(self):
        print("---------------------------------------")
        print("Name : ", self.name)
        print("A/c No. :- ", self.ac)
        print("A/c Type: ", self.type)
        print("Balance: ", self.balance)
        print("Loan Amount: ", self.loan_amt)
        if self.type.lower() == "saving" and self.balance > 5000:
            print("Loan Successfully Granted......")
        else:
            print("Sorry..unable to grant you a loan")


print("---------------- Bank Of Baroda----------------")
name = input("Enter Ur Name: ")
ac = int(input("Enter Ur A/c No. :- "))
Type = input("Enter Account Type:- ")
if not len(str(ac)) == 14:
    exit(0)

print("\n1) View or Update Balance \n2) Fix Deposit \n3) Loan \n4) Exit ")
selection = int(input("\nEnter your selection: "))

Acc = Account(name, ac, Type)

if selection == 1:
    print("Current Balance: ", Acc.balance)
    print("     1)Add Amount\n     2)Withdraw Amount\n     3)Exit")
    choice = int(input("Enter Ur Choice: "))
    amount = int(input("Enter ur Amount : "))
    if choice == 1:
        Acc.deposit(amount)
        print("New Balance: ", Acc.balance)
    elif choice == 2:
        if amount < Acc.balance:
            Acc.withdraw(amount)
        else:
            print("Insufficient Balance")

        print("New Balance: ", Acc.balance)
    elif choice == 3:
        exit(0)
    else:
        print("Invalid Input")

elif selection == 2:
    fd_amt = int(input("Enter Ur FD Amount: "))
    fd = FixDeposit(fd_amt)
    print("     1)Add This Amount Externally\n      2)Deduct This Amount From Ur Current Balance")
    choice = int(input("Enter Ur Choice: "))

    print("Balance: ", fd.balance)
    if choice == 1:
        print(fd_amt)

    elif choice == 2:
        if fd_amt < fd.balance:
            fd.withdraw(fd_amt)
            print("New Balance: ", fd.balance)
        else:
            print("Insufficient Balance")
    else:
        print("Invalid Input")

    fd.display_fd()
    fd.cal_fd()

elif selection == 3:
    loan_amt = int(input("Enter Ur Loan Amount: "))
    ln = Loan(loan_amt)

    ln.display_loan()
    ln.cal_loan()
