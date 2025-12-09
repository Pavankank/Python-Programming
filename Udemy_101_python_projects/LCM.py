def lcm(x,y):
    highest = max(x,y)
    while True:
        if highest % x == 0 and highest % y == 0:
            return highest
        highest = highest + 1
    
a = int(input("Enter first number: "))
b = int(input("Enter second number "))

print(f"The LCM of {a} and {b} is : {lcm(a,b)}")

