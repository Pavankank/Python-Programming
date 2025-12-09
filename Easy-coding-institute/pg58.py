employees = ["Aarav Sharma", "Priya Patel", "Vikram Reddy", "Sanya Gupta", "Rohit Desai",
             "Neha Kumar", "Arjun Nair", "Ananya Singh", "Karan Mehta", "Isha Joshi", "Ishaan Krishna", "Aadriti Kankanala"]

mylist=[]
for name in employees:
    namel=name.lower()
    if namel.startswith('a'):
        mylist.append(name)
print("Names starting with alphabet 'A' or 'a':")
for k in mylist:
    print(k)

mylist=[]
for name in employees:
    namel=name.lower()
    if namel.endswith('a'):
        mylist.append(name)
print("\nNames ending with alphabet 'A' or 'a':")
for k in mylist:
    print(k)

mylist=[]
for name in employees:
    namel=name.lower()
    if 'an' in namel:
        mylist.append(name)
print("\nNames containing 'an':")
for k in mylist:
    print(k)

mylist=[]
for name in employees:
    namel=name.lower()
    if 'sh' in namel:
        mylist.append(name)
print("\nNames containing 'sh':")
for k in mylist:
    print(k)

mylist=[]
for name in employees:
    namel=name.lower()
    if namel.count('a') ==3:
        mylist.append(name)
print(f"\nNames containing three a's:")
for k in mylist:
    print(k)

mylist=[]
for name in employees:
    namel=name.lower()
    if namel.count('a') ==6:
        mylist.append(name)
print(f"\nNames containing four a's:")
for k in mylist:
    print(k)
