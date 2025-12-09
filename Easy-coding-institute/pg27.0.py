n=int(input("Enter a number to see if it is an armstrong or not:"))
a=n
total=0
while n!=0:
	last=n%10
	total=last**3+total
	n=n//10

if a!=total:
	print(a,"is not an armstrong number")
else:
	print(a,"is an armstrong number")
	