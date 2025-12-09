mylist=[5,8,3,9,2,10]

# Largest element:

n=mylist[0]
for k in mylist:
	if k>n:
		n=k	
print("Largest element:",n)

# Smallest element:

n=mylist[0]
for k in mylist:
	if k<n:
		n=k	
print("Smallest element:",n)

