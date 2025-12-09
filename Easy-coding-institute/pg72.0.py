def add():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"{num1} + {num2} = {num1+num2}")

def sub():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"{num1} - {num2} = {num1-num2}")

def multiply():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"{num1} x {num2} = {num1*num2}")

def division():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num2 != 0:
        print(f"{num1} / {num2} = {num1/num2}")
    else:
        print("***************************************")
        print("Error! Division by zero is not allowed.")
        print("***************************************")

def remainder():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    if num2 != 0:
        print(f"{num1} % {num2} = {num1%num2}")
    else:
        print("***************************************")
        print("Error! Division by zero is not allowed.")
        print("***************************************")

def power():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(f"{num1} power {num2} = {num1**num2}")


while True:
    print("***************")
    print("  Calculator")
    print("***************")
    print("1. Add \n2. Substract \n3. Multiply \n4. Divide \n5. Remainder \n6. Power \n7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        add()

    elif choice == '2':
        sub()

    elif choice == '3':
        multiply()
    
    elif choice == '4':
        division()

    elif choice == '5':
        remainder()

    elif choice == '6':
        power()

    elif choice == '7':
        print("Thank you, Have a nice day!")
        break
    else:
        print("That is not a valid choice, please try again!")
