n=int(input("Enter a number to see if it is an armstrong or not:"))

total=0
i = 1
while i==1000:
	j = 1000
	while j!=0:
	last=j%10
	total=last**3+total
	n=n//10

if n==total:
	print(total,"is not an armstrong number")
else:
	print(total,"is an armstrong number")

