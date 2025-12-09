age = int(input("Enter the age of the person to find the category:"))

if age>=0 and age<=3:
	print("The person is an infant")
elif age > 3 and age <=12:
	print("The person is a kid")
elif age > 12 and age <=19:
	print("The person is a teen")
elif age >=20 and age <=40:
	print("The person is an adult")
elif age > 40 and age <=60:
	print ("The person is a middle aged")
else:
	print("The person is a senior citizen")
