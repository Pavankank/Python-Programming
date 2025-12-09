employees = {
    "Emily Chen": ["E001", "Software Engineer", 120000],
    "Liam Patel": ["E002", "Data Scientist", 150000],
    "Ava Lee": ["E003", "Product Manager", 180000],
    "Noah Kim": ["E004", "DevOps Engineer", 140000],
    "Sophia Rodriguez": ["E005", "UX Designer", 100000],
    "Ethan Hall": ["E006", "Business Analyst", 110000],
    "Mia Hernandez": ["E007", "Cybersecurity Specialist", 160000],
    "Lucas Brooks": ["E008", "Network Architect", 170000],
    "Isabella Brown": ["E009", "Database Administrator", 130000],
    "Mason Davis": ["E010", "IT Project Manager", 190000]
}
print("\n##########################################################\n")

empname = input("Enter employee name: ")

print("\n##########################################################\n")
if empname in employees:
    l = employees.get(empname)
    print(f"1. Salary of {empname}: {l[2]}")
else:
    print("Employee not found..")
print("\n##########################################################\n")

if empname in employees:
    l = employees.get(empname)
    print(f"2. Employee ID of {empname}: {l[0]}")
else:
    print("Employee not found..")
print("\n##########################################################\n")

list=[]
for employee, details in employees.items():
    if employee == empname:
        list.append(employee)
        print(f"3. Details of {employee}:\n\n Employee ID --> {details[0]}\n Job Position --> {details[1]}\n Salary --> {details[2]}")

if len(list) == 0:
    print("Employee not found..")
print("\n##########################################################\n")

empid = input("4. Enter Employee ID: ")

for employee, details in employees.items():
    if details[0] == empid:
        print(f"\nEmployee having ID {empid}: {employee}")
        break
else:
    print("Employee not found..")
print("\n##########################################################\n")

names=[]
for empname, details in employees.items():
    if details[2] < 150000:
        names.append(empname)
if len(names) > 0:
    print("5. Employees whose salary is less than 150000:")
    for k in names:
        print(k)
else:
    print("No employee has salary less than 150000.")
print("\n##########################################################\n")