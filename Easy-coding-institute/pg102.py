class InvalidAgeException(Exception):
    "User Defined Exception"

age = int(input("Enter age: "))

try:
    if age < 18:
        raise InvalidAgeException("Under age")
    
except InvalidAgeException as e:
    print(e)

print("rest of the code")
