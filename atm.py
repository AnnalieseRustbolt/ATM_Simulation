import time


def display():
    print("""

░█████╗░████████╗███╗░░░███╗
██╔══██╗╚══██╔══╝████╗░████║
███████║░░░██║░░░██╔████╔██║
██╔══██║░░░██║░░░██║╚██╔╝██║
██║░░██║░░░██║░░░██║░╚═╝░██║
╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝
""")

def start():
    display()
    accpin = "a12#"
    name = input("\tEnter your name:\n\t")
    if not name:
        name = "Guest"
    accbal = input("\tEnter your starting Balance:\n\t€")

    if not accbal or accbal == "" or accbal.isalpha():
        accbal = float(2000)

    accbal = float(accbal)


    transactions = []
    menu(name, accbal, transactions, accpin)

def menu(name,balance, transactions, pin):
    print(f"Greetings, {name}")

    next = input("What would you like to do next? :\na) Print the account balance\nb) Withdraw some money from the account\nc) Deposit some money on the account\nd) Modify the account pin code\ne) View transactions\nf) Quit\n>>> ")
    try:

        if next == "a":
            print("Your balance is €%.2f\n" % (float(balance)))
        elif next == "b":
            balance = withdraw(balance, pin, transactions)
        elif next == "c":
            balance = deposit(balance, pin, transactions)
        elif next == "d":
            pin = modifypin(pin)
        elif next == "e":
            transaction(balance,transactions)
        elif next == "f":
            print("Have a nice day")
            delay()
            exit()
    except ValueError:
        print("Enter a letter")
    menu(name, balance, transactions,pin)

def delay():
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("....")
    time.sleep(1)

def withdraw(balance, pin, transactions):
    pin_input = input("Please enter your pin : ")

    if pin_input == pin:
        withdraw_amount = float(input("How much would you like to withdraw from your account? :"))
        if withdraw_amount > balance:
            print(f"Insufficient funds to complete this request, your balance is € {balance}")
            return balance
        else:
            print("Please wait while your cash is being printed\n")
            balance -= withdraw_amount
            withdraw_amount = "-€" + str(withdraw_amount)
            transactions.append(withdraw_amount)

        delay()
        print("Please remove your cash and take your card")
        print(f">>>Your balance is now € {balance}")
        time.sleep(5)

    return balance

def deposit(balance, pin, transactions):
    pin_input = input("Please enter your pin : ")

    if pin_input == pin:
        dep = float(input("How much would you like to deposit to your account? :"))
        balance += dep
        delay()
        print(f"Deposit successful\n>>>Your balance is now € {balance}")
        time.sleep(5)
        dep = "+€" + str(dep)
        transactions.append(dep)
        return balance

def modifypin(pin):

    pin_input = input("Please enter your pin : ")

    if pin_input == pin:
        x = input("Enter a new pin\n>>> ")
        if validpin(pin) == True:
            pin = x
            delay()

            print(f"Your new pin is {pin}")

            return pin

    else:
        print("Password unchanged")
        return pin

def validpin(pin):


    digit_counter = 0
    alpha_counter = 0
    symbol_counter = 0

    while digit_counter <1 or alpha_counter <1 or symbol_counter <1:


        for letter in pin:


            if letter.isdigit():
                digit_counter = digit_counter + 1

            elif letter.isalpha():
                alpha_counter = alpha_counter + 1
            elif letter == "@" or letter == "#" or letter == "!" or letter == "$":
                 symbol_counter = symbol_counter + 1


        if digit_counter > 0 and alpha_counter > 0 and symbol_counter > 0:
                print("Valid password")
                return True
        else:
            print("Invalid Pin")
            return(False)

def transaction(balance, transactions):
    print("Transactions:")
    for x in transactions:

        if x[0] == "-":
            print('\t\t', x, sep="")
        elif x[0] == "+":
            print('\t\t', x, sep="")
    print("\n\tBalance:€", balance, "\n")
    time.sleep(5)

start()
