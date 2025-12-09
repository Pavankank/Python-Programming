pan=input("Enter PAN number:")

if len(pan) == 10:
    one = pan[0:5]
    two = pan[5:9]
    three = pan[-1]
    if one.isalpha() and two.isnumeric() and three.isalpha():
        print("The entered PAN number is valid.")
    else:
        print("The entered PAN is invalid.")
elif len(pan)==0:
    print("The entered PAN is invalid.")