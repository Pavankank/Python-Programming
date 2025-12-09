word = input("Enter some text:")

if word.isalpha():
    if word.islower():
        print(word.upper())
    else:
        print(word.lower())
else:
    print("Please enter alphabets only")
