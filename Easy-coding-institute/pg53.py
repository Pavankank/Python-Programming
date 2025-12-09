import re # multiple delimiters (split function)

a = "abc@google.com"
b = re.split('[@.]',a)

print(b)