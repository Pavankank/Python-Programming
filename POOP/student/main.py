from student import Student

student1 = Student("Pavan",101,15)
student1.details()
student1.marks(80,90,95,70,84)

print()

student2 = Student("Ishaan",102,15)
student2.details()
student2.marks(90,92,89,87,84)

print()

student3 = Student("Aadriti",103,15)
student3.details()
student3.marks(92,98,97,100,94)

print()

student3 = Student("Ramya",104,16)
student3.details()
student3.marks(80,83,89,92,94)

print()

print(f"My graduating class of {Student.class_start_year}-{Student.class_end_year} has {Student.num_students} students")