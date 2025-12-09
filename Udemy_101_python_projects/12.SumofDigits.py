num = int(input("Enter a number: "))

sum = 0

for digit in str(num):
    sum = sum + int(digit)
print(f"Sum of the digits: {sum}")