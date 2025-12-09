ch=input("Enter a character to find if it is a lower/upper case character or a numeric or a special character:")

if ord(ch)>=65 and ord(ch)<=90:
	print(ch,"is a upper case letter")
elif ord(ch)>=97 and ord(ch)<=122:
	print(ch,"is a lower case letter")
elif ord(ch)>=48 and ord(ch)<=57:
	print(ch,"is a numeric value")
else:
	print(ch,"is a special character")
