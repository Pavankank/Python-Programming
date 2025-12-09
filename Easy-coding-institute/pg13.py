ch=input("Enter an alphabet to convert it to upper or lower case:")

if ord(ch)>=65 and ord(ch)<=90:
	print(ch,"has been converted to",chr(ord(ch)+32))
elif ord(ch)>=97 and ord(ch)<=122:
	print(ch,"has been converted to",chr(ord(ch)-32))
else:
	print(ch,"is not an alphabet!!")
