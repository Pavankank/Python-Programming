import random

rand = random.randrange(1,101)
print(rand)
print("Guess a number between 1 and 100... ")
n=0

while n<5:
    a = int(input(f"Attempt {n+1}: "))
    if a != rand and a < 101:
        print("Guess again!")
        if n == 3:
            a = int(input("This is the final attempt: "))
            if a != rand:
                print("Good bye!")
                n = 4
            else:
                print("Your guess is right!")
                break
    elif a == rand:
        print("Awesome!! Your guess is right!")
        break
    else:
        print("Stupid! Enter number between 1 and 100 only.")
    n+=1
        

