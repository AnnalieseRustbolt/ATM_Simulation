from time import sleep


def start():
    load()
    name = input("\tEnter your name:\n\t")
    if not name:
        name = "Sawyer Thomson"
    balance = input("\tEnter your starting Balance:\n\t€")

    if not balance:
        balance = 204.90
    transactions = []
    menu(name, balance, transactions)


def load():
    print("""

░█████╗░████████╗███╗░░░███╗
██╔══██╗╚══██╔══╝████╗░████║
███████║░░░██║░░░██╔████╔██║
██╔══██║░░░██║░░░██║╚██╔╝██║
██║░░██║░░░██║░░░██║░╚═╝░██║
╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝
""")


def loading():
    for x in range(10):
        print("\n\n")
        print("\t*" * x)
        sleep(.1)
        print('\x1bc')


def menu(name, balance, transactions):
    loading()
    print(f"Greetings, {name}.", "your balance is €%.2f\n" % (float(balance)))
    print('Choose an command from the menu:', '1) Withdraw', '2) Deposit', '3) Calculate interest',
          '4) Transaction history', '5) Exit', sep="\n\t")
    option = input(">")
    try:
        option = int(option)
        if option == 1:
            balance = withdraw(balance, transactions)
        elif option == 2:
            balance = deposit(balance, transactions)
        elif option == 3:
            interest(balance)
        elif option == 4:
            transaction(balance, transactions)
        elif option == 5:
            load()
            exit()
        else:
            print("invalid option")
    except ValueError:
        print("Enter a number")
    menu(name, balance, transactions)


def withdraw(balance, transactions):
    withdraw = float(input("\nHow much would you like to withdraw\n\t€"))
    if withdraw > balance:
        print("insufficient funds")
    else:
        balance -= withdraw
        withdraw = "-" + str(withdraw)
        transactions.append(withdraw)
    return balance


def deposit(balance, transactions):
    dep = int(input("\nHow much would you like to deposit\n\t€"))
    balance += dep
    dep = "+" + str(dep)
    transactions.append(dep)
    return balance


def interest(balance):
    print("\nAfter one year you would have %.2f\n\n" % (balance * 1.15))
    sleep(3)


def transaction(balance, transactions):
    print("Transactions:")
    for x in transactions:

        if x[0] == "-":
            print('\t\t', x, sep="")
        elif x[0] == "+":
            print('\t\t', x, sep="")
    print("\n\tBalance:", balance, "\n")
    sleep(5)


start()