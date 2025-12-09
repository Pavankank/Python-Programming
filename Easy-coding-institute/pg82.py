# f = open("/Users/kankanala/Documents/Python-Programming/myfile.txt")
# print(f.read())

# p = open("/Users/kankanala/Documents/Python-Programming/myfile.txt","w")
# text = input("Enter some text: ")

# p.write(text)
# print("write successful")
# p.close()

# r = open("/Users/kankanala/Documents/Python-Programming/myfile.txt","r")
# w = open("/Users/kankanala/Documents/Python-Programming/myfile1.txt","w")

# w.write(r.read())
# w.close()
# r.close()
# print("Copied Successfully..")

# r = open("/Users/kankanala/Documents/Python-Programming/myfile.txt","r")
# w = open("/Users/kankanala/Documents/Python-Programming/myfile1.txt","a")

# w.write("\n"+r.read())
# w.close()
# r.close()
# print("Copied Successfully..")

# import re

# data = open("/Users/kankanala/Documents/Python-Programming/myfile.txt")

# text = data.read()

# words = text.split()

# words = re.split('[" "\n]', text)

# lines = re.split('[\n]', text)

# print(words)
# print(lines)

# print(len(words))
# print(len(lines))

import re

data = open("/Users/kankanala/Documents/Python-Programming/myfile.txt")

text = data.read()

words = text.split()

words = text.split()

lines = text.split()

print(words)
print(lines)

print(len(words))
print(len(lines))