# Dynamic code
	
counter = int(input("Enter a number to find armstrong numbers: "))	

while counter >= 1:
	n = len(str(counter))
	num = counter
	total = 0
	while num!=0:
		last = num % 10
		total = total + last**n
		num = num // 10

	if total == counter:
		print(f"{counter} is an armstrong number.")
	counter = counter - 1