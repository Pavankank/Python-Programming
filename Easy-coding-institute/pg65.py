employees = {
    "Alice Johnson": "555-1234",
    "Bob Smith": "555-5678",
    "Charlie Brown": "555-8765",
    "Diana Prince": "555-4321",
    "Eve Adams": "555-2468",
    "Frank Miller": "555-1357",
    "Grace Lee": "555-8642",
    "Hank Roberts": "555-3698",
    "Ivy Davis": "555-9087",
    "Jack Wilson": "555-7420"
}

name=input("Enter employee name:")

if name in employees:
    print(name,"->",employees.get(name))
else:
    print("Name not found!!")

