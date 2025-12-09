class Employee:

    def insert(self,e,n,j,s):
        self.empid = e
        self.empname = n
        self.job = j
        self.salary = s

    def showDetails(self):
        print("Employee details:\n*****************\n")
        print(f"Employee ID -> {self.empid}, Empname -> {self.empname}, Job -> {self.job}, Salary -> {self.salary}\n")

    def getSalary(self):
        print(f"{self.empname}'s salary is {self.salary}\n")

    def setSalary(self,s):
        self.salary = s
        print(f"Salary of employee {self.empname} is set to {self.salary}\n")


emp1 = Employee()
emp1.insert(101,"Allu Arjun","Sr. Cloud Support Engineer",200000)
emp1.showDetails()
emp1.getSalary()
emp1.setSalary(150000)
emp1.showDetails()


emp2 = Employee()
emp2.insert(102,"Prabhas","Technical Support Engineer",100000)
emp2.showDetails()
emp2.getSalary()
emp2.setSalary(250000)
emp2.showDetails()





        

