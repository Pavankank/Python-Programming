class Employee:
    def __init__(self,empid,name,job,sal):   # Contructor: special method that generally used to initialize instance vairbale
        self.empid = empid
        self.name = name
        self.job = job  
        self.sal = sal

    def showDetails(self):
        print(self.empid, self.name, self.job, self.sal)

emplist = []

while True:
    print("\n1. Add Record \n2. Delete Record \n3. Display Records \n4. Exit")
    option = int(input("Choose your option [1-4]: "))

    if option == 1:
        eid = int(input("Enter empid: " ))
        name = input("Enter name: ")
        job = input("Enter job: ")
        sal = float(input("Enter salary: "))
        emplist.append(Employee(eid,name,job,sal))
        print("Record added successfully..")

    # if option == 2:
    #     index = int(input("Which record you want to delete: "))
    #     if len(emplist) < index:
    #         print(f"sorry..{len(emplist)} records are present")
    #     else:
    #         emplist.pop(index-1)
    #         print("Record deleted successfully!!")

    if option == 2:
        eid = int(input("Enter employee ID: "))
        for obj in emplist:
            if emplist[0] == eid:
                del emplist[eid]


    if option == 3:
        for item in emplist:
            item.showDetails()

    if option == 4:
        print("Thanks you!!")
        break
