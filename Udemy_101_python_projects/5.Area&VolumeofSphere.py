import math

while True:
    try:
        r = float(input("Enter radius of the sphere: "))
        volume = (4/3) * math.pi * r**3
        area = 4 * math.pi * r**2
        print(f"Area of the sphere: {area:.2f}")
        print(f"Volume of the sphere: {volume:.2f}")
        break
    except ValueError as v:
        print(v)
