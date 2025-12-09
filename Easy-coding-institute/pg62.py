line = "jack and jill went up the hill. jack fell down and jill saved jack"

mywords = line.split(' ')
unique_words = set(mywords)

print(unique_words)

for word in mywords:
    print(word," ", line.count(word))

myletters = list(line)
myuniqueletters = set(myletters)

for k in myuniqueletters:
    print(k, " -> ", line.count(k))