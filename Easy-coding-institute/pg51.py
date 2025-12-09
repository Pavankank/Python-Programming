statement = "I got 97 in maths, 85 in science and 71 in English"

words=statement.split(' ')

total =0

for word in words:
    if word.isnumeric():
        total = total + int(word)

print("sum of the subjects:",total)


