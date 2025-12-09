import random

secret_number = random.randrange(1,101)
print(secret_number)

print("Welcome to the number guessing game!")
print("I have chosen a number between 1 and 100. Can you guess it?")

attempts = 0

while True:
    guess = input("Enter your guess or type 'quit' to exit: ")
    if guess.lower() == 'quit':
        print(f"You gave up! The chosen secret number was {secret_number}.")
        break
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number between 1 and 100")
        continue
    attempts += 1

    if guess == secret_number:
        print(f"Congrats! You guessed the number in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again")
