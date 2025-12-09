class Student:

    class_start_year = 2025
    class_end_year = 2026
    num_students = 0

    def __init__(self,name,rollno,age):
        self.name = name
        self.rollno = rollno
        self.age = age
        Student.num_students += 1
    
    def details(self):
        print(f"Student Name: {self.name}, Roll No.: {self.rollno}, Age: {self.age}, Year: {Student.class_start_year}-{Student.class_end_year}")

    def marks(self,maths,science,social,english,hindi):
        self.maths = maths
        self.science = science
        self.social = social
        self.english = english
        self.hindi = hindi
        Total = self.maths + self.science + self.social + self. english + self.hindi
        print(f"--------------\n{self.name}'s marks\n--------------\nMaths: {self.maths}\nScience: {self.science}\nSocial: {self.social}\nEnglish: {self.english}\nHindi: {self.hindi}")
        print(f"--------------\nTotal: {Total}\n--------------\nPercentage: {Total/5}%")




        