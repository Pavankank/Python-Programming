while True:
    try:
        l = float(input("Enter length of the parallelogram: "))
        b = float(input("Enter heigth of the parallelogram: "))
        area = l * b
        print(f"Area of the parallelogram: {area}")
        break
    except ValueError:
        print("Enter digits only")

    