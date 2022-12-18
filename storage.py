import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Madeline@()6421",
    database="gpacalculator"
)

mycursor = mydb.cursor()

#CREATES DATABASE RELATIONS
# mycursor.execute("CREATE TABLE Department (departmentName VARCHAR(50), building VARCHAR(20), PRIMARY KEY(departmentName))")
# mycursor.execute("CREATE TABLE Instructor (instructorId VARCHAR(50) NOT NULL, fname VARCHAR(50) NOT NULL, lname VARCHAR(50) NOT NULL, course VARCHAR(50), department VARCHAR(50) NOT NULL, PRIMARY KEY(instructorId), FOREIGN KEY (department) REFERENCES Department(departmentName))")
# mycursor.execute("CREATE TABLE Course (courseNumber VARCHAR(50) NOT NULL, courseName VARCHAR(50) NOT NULL, credits int, instructor VARCHAR(50), PRIMARY KEY(courseNumber), FOREIGN KEY (instructor) REFERENCES Instructor(instructorId))")
# mycursor.execute("CREATE TABLE Student (studentId VARCHAR(25) NOT NULL, fname VARCHAR(50) NOT NULL, lname VARCHAR(50) NOT NULL, course VARCHAR(50), PRIMARY KEY(studentId), FOREIGN KEY(course) REFERENCES Course(courseNumber))")

#user command runs until exit command is initiated 

while True:
    print("------------------\n|Commands:       |\n|create-student  |\n|add-course      |\n|update-grade    |\n|delete-course   |\n|delete-student  |\n|quit             |\n------------------")
    cmd = input("Enter a command -> ")
    cmd = cmd.lower()
    #Checks if user entered quit

    match cmd:
        case "create-student":
            #code goes here
            continue
        case "add-course":
            #code goes here
            continue
        case "update-grade":
            #grade goes here
            continue
        case "delete-course":
            #delete student goes here
            continue
        case "quit":
            print ("Exitting program...")
            break




