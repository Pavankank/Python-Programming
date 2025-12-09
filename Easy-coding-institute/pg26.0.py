first,second,total = 0,1,0

n = int(input("Enter length of the series: "))
print(f"Fibonacci series for length {n}:")
while n!=0:
	print(total,end=' ')
	first = second
	second = total
	total = first + second
	n = n - 1

print()