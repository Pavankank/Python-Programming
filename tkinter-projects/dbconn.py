import mysql.connector
from datetime import date
import datetime

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "sys99tem",
    database = "pythondb"
)

mycursor = db.cursor()
# mycursor.execute("CREATE TABLE dataentry (Student_ID int PRIMARY KEY AUTO_INCREMENT, Title varchar(10), First_Name varchar(25), Last_Name varchar(25), Age int UNSIGNED, Nationality varchar(25), Num_Courses int UNSIGNED, Num_Semesters int UNSIGNED, Reg_Status varchar(25))")
# mycursor.execute("DESCRIBE dataentry")
# mycursor.execute("INSERT INTO dataentry (Title, First_Name, Last_Name, Age, Nationality, Num_Courses, Num_Semesters, Reg_Status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", ("Mr.", "Pavan", "Kankanala", 40, "India", 30, 4, "Registered"))
# db.commit()

mycursor.execute("SELECT * FROM dataentry")

# mycursor.execute("drop table dataentry")

for x in mycursor:
     print(x)