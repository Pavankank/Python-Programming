text="I love running, running is my passion, I go running every day, running through the park, running past the trees, running with my friends, running is what I love, I love running, running is my life."

word = input("Enter a word to find if it is present in the sentence or not:")

if text.count(word) > 0:
    print (f"{word} is present in the sentence.")
else:
    print (f"{word} is not present")
print(f"Total count of the word '{word}' in the sentence: {text.count(word)}")

