import os, sys, time, logging
from datetime import datetime
import re

# Ask user to insert card
# Ask for PIN
# Choose to show balance, deposit, or withdraw
# Ask if they want another transaction
# Repeat if yes, exit if no

#  starting screen
print(datetime.now())
time.sleep(0.7)
print("Please insert your debit card...")
time.sleep(1.4)
print("Verifying card...")
time.sleep(2)
print("Verified!")

approved = True


def home_display():
    logged_in = True
    balance = int(20000)

    time.sleep(1)
    print("What would you like to do? ")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")

    selection = int(input("Enter 1-4: \n"))

    match selection:
        case 1:
            #  check balance
            time.sleep(0.3)
            print(f"Your balance is {balance}")
            while logged_in:
                selection = input("Would you like another transaction? (yes/no) : ").lower()
                if selection == "yes":
                    time.sleep(0.8)
                    home_display()
                elif selection == "no":
                    sys.exit()
                    logged_in = False
                else:
                    print("Enter yes or no")
        case 2:
            #  deposit
            while logged_in:
                time.sleep(0.8)
                deposit = input("Please enter deposit amount: ")
                print(f"You deposited {deposit}")
                selection = input("Would you like another transaction? (yes/no) : ").lower()
                if selection == "yes":
                    time.sleep(0.8)
                    home_display()
                elif selection == "no":
                    sys.exit()
                    logged_in = False
                else:
                    print("Enter yes or no")
        case 3:
            time.sleep(0.8)
            withdraw = input("Please enter withdrawal amount: ")
            print(f"You withdrew {withdraw}")
            while logged_in:
                selection = input("Would you like another transaction? (yes/no) : ").lower()
                if selection == "yes":
                    time.sleep(0.8)
                    home_display()
                elif selection == "no":
                    sys.exit()
                    logged_in = False
                else:
                    print("Enter yes or no")


def get_pin():
    nums = [1234, 5678, 5432, 4321, 1111, 1357, 2468]

    try:
        user_pin = input("Please enter your PIN: ")
        # print(len(user_pin))
        if len(user_pin) > 4:
            print('Invalid input. Please try again')
    except ValueError:
        if user_pin.isalpha():
            print('Invalid input. Numbers only')
    else:
        print("Checking PIN...")
        time.sleep(0.3)

        if int(user_pin) in nums:
            print(f"Hello, welcome to your account")
            home_display()


get_pin()








