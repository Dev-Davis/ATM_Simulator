
loggedIn = False

userSavings = float(20000.00)
x = 0


def homeDisplay():
    print("What would you like to do? ")
    print("1. View checking")
    print("2. View savings")
    print("3. Withdraw")
    print("4. Exit")

    selection = int(input("Please enter a number: \n"))
    user_checking = float(3500.00)

    match selection:
        case 1:
            print(user_checking)
            input("Press any button to go home...")
        case 2:
            print(userSavings)
            input("Press any button to go home...")
        case 3:
            withdraw_amount = float(input("How much would you like to withdraw? \n"))
            user_checking = user_checking - withdraw_amount
            print(user_checking)
            input("Press any button to go home...")
        case 4:
            print("Thanks for using the ATM. Goodbye!")
        case _:
            print("Your input was invalid. Try again")
            input("Press any button to go home...")


#  runs 3 times then locks account (figure out scope for locking account
while x <= 2:
    print("Welcome to the ATM. Please log in...")
    username = input("Enter Username: ")
    password = input("Enter Password: ")


    if username == "Dott" and password == "logitin":
        print(f"Hello {username}, Welcome to Tha Bank")
        loggedIn = True
        break
    else:
        print("Username or Password did not match")
    x += 1
    # print(x)

    if x > 2:
        print("We've temporarily locked your account")
        loggedIn = False
        print(loggedIn)

while loggedIn:
    homeDisplay()







