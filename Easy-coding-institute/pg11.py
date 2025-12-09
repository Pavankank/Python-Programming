maths=int(input("Enter maths marks:"))
chem=int(input("Enter chem marks:"))
phy=int(input("Enter phy marks:"))

total = maths + chem + phy
per = total/3

if maths < 40 or chem < 40 or phy < 40:
	print("The person failed in at-least one subject!!")
else:
	print("The student’s percentage is:",per,"%")
