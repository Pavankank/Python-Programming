i=1
total = 0
while i<=6:
	mark = int(input("Enter marks for subject:"))
	total = total + mark
	i = i + 1
print("Total=",total)
print("Percentage=",total/6)

print()

total = 0
for i in range(1,6):
	mark = int(input(f"Enter marks for subject {i}: "))
	total = total + mark
print(f"Total: {total}")
print(f"Percentage: {total/6}")
