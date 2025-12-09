counter = 0	

print ("Palindrome numbers between 0 to 1000: ")
while counter <= 1000:
	num = counter
	rev = 0
	while num!=0:
		last = num % 10
		rev = rev * 10 + last
		num = num // 10

	if rev == counter:
		print(f"{counter} is a palindrome number.")
	counter = counter + 1