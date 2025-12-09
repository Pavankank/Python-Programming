a = 5
b = 2
print(a/b) # No error with this code

# a = 5
# b = 0
# print(a/b) # This will get exception, there might be code running after this error
# print("Rest of the code..")

a = 5
b = 0
try:
    print(a/b)
except ZeroDivisionError:
    print("Hey don't give zero in the denominator")
print("Rest of the code..")

a = None
try:
    len(a)
except:
    print("Type error")
print("Rest of the code")

try: # This will handle error if you give character as input
    num = int(input("Enter a number"))
    res = num * 5
    print(res)
except:
    print("value error")

print("rest of the code")

arr = [5,2,6,2,8]
try:
    for i in range(6):
        print(arr[i], end=" ")
except:
    print("Index out of bounds")
print ("rest of the code")