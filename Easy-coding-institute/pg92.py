class Parent:
    def abc(self):
        print("abc method of parent class")

class Child(Parent):
    def xyz(self):
        print("xyz of child class")

c = Child()
c.xyz()
c.abc()
