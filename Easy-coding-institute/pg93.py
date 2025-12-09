class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, eid, job, sal):
        super().__init__(name,age)
        self.eid = eid
        self.job = job
        self.sal = sal

    def showDetails(self):
        print(self.name, self.age, self.eid, self.job, self.sal)

e = Employee("Pavan", 25, 555, "Analyst", 52345.23)
e.showDetails()
