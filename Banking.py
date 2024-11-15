import os, sys, time, logging
from datetime import datetime

##############
# To do list #
##############

# Ask user to insert card
# Ask for PIN
# Choose to show balance, deposit, or withdraw
# Ask if they want another transaction
# Repeat if yes, exit if no

# user_savings = float(20000.00)
# user_balance = float(3500.00)
# current_balance = None
# x = 0

print(datetime.now())
time.sleep(0.7)
print("Please insert your debit card...")
time.sleep(3)
print("Verifying card...")
time.sleep(2)


def home_display():
    logged_in = True
    balance = int(20000)

    time.sleep(1)
    print("What would you like to do? ")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    selection = int(input("Enter 1-4: \n"))

    match selection:
        case 1:
            #  check balance
            time.sleep(1)
            print(f"Your balance is {balance}")
            while logged_in:
                selection = input("Would you like another transaction? (yes/no) : ").lower()
                if selection == "yes":
                    time.sleep(0.8)
                    home_display()
                elif selection == "no":
                    break
                else:
                    print("Enter yes or no")
        case 2:
            #  deposit
            time.sleep(1)
            deposit = input("Please enter deposit amount: ")
            print(f"You deposited {deposit}")
            while logged_in:
                selection = input("Would you like another transaction? (yes/no) : ").lower()
                if selection == "yes":
                    time.sleep(0.8)
                    home_display()
                elif selection == "no":
                    break
                else:
                    print("Enter yes or no")
        case 3:
            time.sleep(1)
            withdraw = input("Please enter withdrawal amount: ")
            print(f"You withdrew {withdraw}")
            while logged_in:
                selection = input("Would you like another transaction? (yes/no) : ").lower()
                if selection == "yes":
                    time.sleep(0.8)
                    home_display()
                elif selection == "no":
                    break
                else:
                    print("Enter yes or no")


def get_pin():
    approved = True
    nums = [1234, 5678, 5432, 4321, 1111, 1357, 2468]

    user_pin = int(input("Please enter your PIN: "))
    print("Checking PIN...")
    time.sleep(1)
    while approved:
        try:
            if user_pin in nums:
                print(f"Hello, welcome to your account")
                home_display()
            else:
                print("Incorrect PIN")
        except Exception as e:
            print('Numbers only for PIN')


get_pin()







