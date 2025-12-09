mylist=[7,3,9,10,33,1,93,4,23,25,67]

for i in range(len(mylist)):
	for j in range(i,len(mylist)):
		if mylist[i] > mylist[j]:
			temp = mylist[i]
			mylist[i] = mylist[j]
			mylist[j] = temp

for k in mylist:
	print(k,end=" ")
print()

