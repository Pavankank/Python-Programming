def show_balance():
    print(f"\nCurrent Account Balance: ${float(balance)}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("\nThat's not a valid amount")
        return 0.00
    else:
        a = (f"${amount} has been deposited into your account.")
        print(a)
        mytxnlist.append(a)
        return amount

def withdraw():
    amount = float(input("Enter an amount to be withdrawn: "))

    if amount > balance:
        print("\nInsufficient funds!")
        return 0.00
    else:
        a = (f"${amount} has been withdrawn from your account.")
        print(a)
        mytxnlist.append(a)
        return amount

balance = 0.00
mytxnlist = []

while True:
    print("\n*******************")
    print("  Banking Program")
    print("*******************")

    print("1. Show Balance \n2. Deposit \n3. Withdraw \n4. Check Transactions \n5. Exit")

    choice = input("\nEnter your choice [1-4]: ")

    if choice == '1':
        show_balance()

    elif choice == '2':
        balance = balance + deposit()

    elif choice == '3':
        balance = balance - withdraw()

    elif choice == '4':
        print("\nRecent Transactions:\n")
        for k in mytxnlist:
            print(k)
            
    elif choice == '5':
        print ("\nThank you, Have a nice day!\n")
        break

    else:
        print("That is not a valid choice, please try again")