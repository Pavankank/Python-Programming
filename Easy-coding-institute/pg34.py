for i in range(5):
	for j in range(0,i+1):
		print("*", end=" ")
	print()

print()

for i in range(5):
	for j in range(5,i,-1):
		print("*", end=" ")
	print()

print()

for i in range(5):
	for j in range(5,i,-1):
		print(" ", end=" ")
	for k in range(i+1):
		print("*", end=" ")
	print()
print()
print("\n")

for i in range(5):
	for j in range(5,i,-1):
		print(" ", end=" ")
	for k in range(i+1):
		print("*", end=" ")
	for l in range(6,6-i,-1):
		print("*", end=" ")
	print() 
print()
print("\n")

n=int(input("Enter a pattern size:"))

for i in range(n):
	for j in range(n,i,-1):
		print(" ", end=" ")
	for k in range(i+1):
		print("*", end=" ")
	for l in range(n+1,n+1-i,-1):
		print("*", end=" ")
	print() 
print("\n")

for i in range(5):
	for j in range(5,i+1,-1):
		print(" ", end=" ")
	for k in range(i+1):
		print("*", end=" ")
	for l in range(6,6-i,-1):
		print("*", end=" ")
	print()
print("\n")

for i in range(5):
	for j in range(5,i,-1):
		print("*", end=" ")
	for l in range(4,i,-1):
		print("*", end=" ")
	print()
	for k in range(i+1):
		print(" ", end=" ")
print("\n")