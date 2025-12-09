num = int(input("Enter a number to find its factors: "))
print(f"Factors of the {num}: ")
for k in range(1, num+1):
    if num % k == 0:
        print(k, end = " ")
print()
