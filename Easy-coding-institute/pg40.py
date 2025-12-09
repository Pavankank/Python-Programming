a=[5,2,9,7,1]
print(a)

for i in range (len(a)):
	temp = a[0]
	for j in range(0,4):
		a[j] = a[j+1]
	a[4] = temp
print(a)
