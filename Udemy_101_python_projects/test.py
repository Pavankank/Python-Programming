try: # This will handle error if you give character as input
    num = int(input("Enter a number: "))
    res = num * 5
    print(res)
except ValueError:
    print("Enter digits only")

print("rest of the code")