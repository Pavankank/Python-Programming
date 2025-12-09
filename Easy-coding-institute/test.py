i=1
f=0
total=0
while (i<=6):
	sub=int(input(f"Enter the marks of student's subject {i}: "))
	if sub>100:
		print("Please enter correct marks of the subject")
		continue
	total=total+sub
	i=i+1
	if sub<40:
		f=f+1	
per=total/6
print("Total Marks:",total)
print("Percentage:",per)
if f==0:
	if per>=90:
		print("The student has passed in Distinction!")
	elif per>=80 and per<90:
		print("The student has passed in First Class!")
	elif per>=70 and per<80:
		print("The student has passed in Second Class!!")
	else:
		print("The student has passed in Third Class!!!")
else:
	print(f"The student has failed in {f} subjects")

