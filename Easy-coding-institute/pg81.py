import random

print("Your OTP is", end=' ')

for k in range(6):
    print(random.randrange(0,9), end='')
print()