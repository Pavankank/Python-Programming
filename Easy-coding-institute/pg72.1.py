def calculator():
    while True:
        print("\nChoose an option to perform:")
        print("1. Add")
        print("2. Subtract")
        print("3. Divide")
        print("4. Multiply")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice in [1, 2, 3, 4]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                print(f"{num1} + {num2} = {num1 + num2}")
            elif choice == 2:
                print(f"{num1} - {num2} = {num1 - num2}")
            elif choice == 3:
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 / num2}")
                else:
                    print("Error! Division by zero is not allowed.")
            elif choice == 4:
                print(f"{num1} * {num2} = {num1 * num2}")
        elif choice == 5:
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please choose again.")

calculator()