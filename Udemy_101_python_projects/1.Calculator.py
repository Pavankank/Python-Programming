def add():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    total = num1 + num2
    print(f"{num1} + {num2} = {total}")

def sub():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    total = num1 - num2
    print(f"{num1} - {num2} = {total}")

def mul():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    total = num1 * num2
    print(f"{num1} x {num2} = {total}")

def div():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 == 0:
        print("Error! Division by zero is not allowed, please try again.")
    else:
        total = num1 / num2
        print(f"{num1} / {num2} = {total}")

def quo_rem():
    num1 = float(input("Enter Dividend: "))
    num2 = float(input("Enter Divisor: "))
    Quo = num1 // num2
    Rem = num1 % num2
    print(f"Quotient = {Quo}\nRemainder = {Rem}")

def pow():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    total = num1 ** num2
    print(f"{num1} to the power of {num2} = {total}")

def sqroot():
    num1 = float(input("Enter number to find its square root: "))
    total = num1**0.5
    print(f"Square root of {num1} = {total}")

def cuberoot():
    num1 = float(input("Enter number to find its square root: "))
    total = num1**0.3333333333333334
    print(f"Cube root of {num1} = {total}")

while True:
    print(f" ************** \n*| Calculator |*\n ************** ")
    print(f"1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Quotient & Remainder\n6. Power\n7. Square Root\n8. Cube Root\n9. Exit")
    choice = input(f"Choose your option [1-9]: ")

    if choice == '1':
        add()
    elif choice == '2':
        sub()
    elif choice == '3':
        mul()
    elif choice == '4':
        div()
    elif choice == '5':
        quo_rem()
    elif choice == '6':
        pow()
    elif choice == '7':
        sqroot()
    elif choice == '8':
        cuberoot()
    elif choice == '9':
        print("Have a good day!")
        break
    else:
        print("Choose the right option.")