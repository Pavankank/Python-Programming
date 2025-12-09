n = int(input("Enter the number of terms: "))

f1 = 0
f2 = 1
for k in range(n):
    print(f1, end=" ")
    f1,f2 = f2, f1+f2