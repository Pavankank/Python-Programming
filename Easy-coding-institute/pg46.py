mylist = [
    ["222","Pavan",34324.23,"Analyst"],
    ["532","Ramya",63244.23,"TeamLead"],
    ["863","Ishaan",95874.23,"Manager"],
    ["146","Aadriti",42356.23,"Admin"]
]

empid=input("Enter the employee ID:")

for k in mylist:
    if k[0]==empid:
        print(k[1],"'s designation is",k[3])
        break
else:
    print("Employee not found..\n")
print()

list=[]
for k in mylist:
    if k[2] < 70000:
        list.append(k)
print(list[1],list[2])
        # print(k[1],"'s salary is",k[2])