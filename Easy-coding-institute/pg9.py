s1=int(input("Enter subject 1 marks:"))
s2=int(input("Enter subject 2 marks:"))
s3=int(input("Enter subject 3 marks:"))

total=s1+s2+s3
per=total/3

print("Percentage:",per,"%")

if per >=90 and per<=100:
	print("A++ Grade")
elif per >=80 and per <90:
	print("A+ Grade")
elif per >=70 and per <80:
	print("A Grade")
elif per >=60 and per <70:
	print("B Grade")
elif per >=50 and per <60:
	print("C Grade")
else:
	print("No Grade")
