class Student:

    def insert(self,r,n,p): #self: it refers to current object
        self.rollno = r
        self.name = n
        self.perc = p
    
    def showDetails(self):
        print("Percentage ->",self.perc,", Details ->",self.rollno, "|",self.name)

# How to create an object

std1 = Student()

std1.insert("001","Pavan Kank",88)

std1.showDetails()

std2 = Student()

std2.insert("002","Ishaan Krishna",95)

std2.showDetails()