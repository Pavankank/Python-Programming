s1=int(input("Enter number 1:"))
s2=int(input("Enter number 2:"))
s3=int(input("Enter number 3:"))

if s1>s2 and s1>s3:
	print(s1,"is highest")
elif s2>s1 and s2>s3:
	print(s2,"is highest")
elif s3>s1 and s3>s2:
	print(s3,"is highest")
else:
	print("Two or more numbers are same")
