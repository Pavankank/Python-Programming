r = open("/Users/kankanala/Documents/Python-Programming/Easy-coding-institute/student-info.txt")
data = r.read()

words = data.split()
marks=[]
total = 0
for k in words:
    if k.isnumeric() and len(k)==2:
        total = total + int(k)

print(f"Total Marks: {total}\nPercentage: {total/5}%")

inword=input("Enter a word to find it in the file: ")

for word in words:
    if inword == word:
        print(f"'{inword}' word found")
        break
else:
    print("Word not found!")