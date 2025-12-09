import math

while True:
    try:
        r = float(input("Enter radius of the cylinder: "))
        h = float(input("Enter height of the cylinder: "))
        volume = math.pi * r * r * h
        area = (2 * math.pi * r * h) + (2 * math.pi * r * r)
        print(f"Volume of the cylinder: {round(volume,2)}")
        print(f"Area of the cylinder: {round(area,2)}")
        break
    except ValueError as v:
        print(v)