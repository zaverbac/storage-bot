import mysql.connector
import tkinter as tk
from tkinter import *
import tkinter.messagebox as message

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Madeline@()6421",
    database="gpacalculator"
)

user = ""
mycursor = mydb.cursor(buffered=True)

#Does course check to see if it already exists
def logout():
    calculator_frame.destroy()
    create_login()

def checkCourses(username, course, grade, credits):
    mycursor.execute("SELECT * FROM class WHERE userId = %s AND class_name = %s", (username, course))
    result = mycursor.fetchall()
    if len(result) > 0:
        return message.showinfo("Error", "You already have " + course + " as a registered class")
    else:
        mycursor.execute("INSERT INTO class (class_name, userId, credits, grade) VALUES (%s, %s, %s, %s)", (course, username, credits, grade)), mydb.commit()
        course_frame.destroy()
        gpaCalculator(username)
        return message.showinfo("Success", course + " added successfully")
def addCourse(username):
    global course_frame
    course_frame = Frame(calculator_frame, width=500, height=400)
    course_frame.grid(row=1, column=0, sticky="NW")
    course_frame.grid_propagate(0)
    course_frame.update()
    
    course_label = Label(course_frame, text="Course Name: ")
    course_label.place(x=250, y=10, anchor="center")
    course = Entry(course_frame, width=20)
    course.place(x=250, y=30, anchor="center")
    
    grade_label = Label(course_frame, text="Grade: ")
    grade_label.place(x=250, y=60, anchor="center")
    grade = Entry(course_frame, width=20)
    grade.place(x=250, y=80, anchor="center")
    
    credits_label = Label(course_frame, text="Credits: ")
    credits_label.place(x=250, y=110, anchor="center")
    credits = Entry(course_frame, width=20)
    credits.place(x=250, y=130, anchor="center")
    
    add = Button(course_frame, text="Add Course", command=lambda: checkCourses(username, course.get(), grade.get(), credits.get()))
    add.place(x=250, y=160, anchor="center")
    
    logout_button = Button(course_frame, text="Logout", command=lambda: logout())
    logout_button.place(x=250, y=190, anchor="center")
    
    
def gpaCalculator(username):
    global calculator_frame
    calculator_frame = Frame(window, width=500, height=400)
    calculator_frame.grid(row=1, column=0, sticky="NW")
    calculator_frame.grid_propagate(0)
    calculator_frame.update()
    
    query = mycursor.execute("SELECT * FROM class WHERE userId = %s", (username,))
    if  query == None:
        #Display no courses added
        empty = Label(calculator_frame, text="No courses added", font=("Arial", 18, "bold"), fg="red")
        empty.place(x=250, y=10, anchor="center")
    else:
    #Display courses
       query = mycursor.fetchall()
       for x in query:
           course = Label(calculator_frame, text=x[1])
           course.place(x=250, y=10, anchor="center") 
        
    global add_course    
    add_course = Button(calculator_frame, text="Add Course", command=lambda: addCourse(username))
    add_course.place(x=250, y=40, anchor="center")

def loginCheck(username, password):
    if username == "" or password == "":
        message.showinfo("Error", "Please enter a username and password")
        return
    
    mycursor.execute("SELECT * FROM user WHERE username = %s AND password = %s", (username, password))
    result = mycursor.fetchall()
    if len(result) > 0:
        message.showinfo("Success", "Login successful")
        login_frame.destroy()
        
        gpaCalculator(username)
    else:
        message.showinfo("Error", "Incorrect username or password")

def addUser(username, password):
    if username == "" or password == "":
        message.showinfo("Error", "Please enter a username and password")
        return
    
    if len(username) > 20 or len(username) < 6:
        message.showinfo("Error", "Username must be between 3 and 20 characters")
        return
    
    if len(password) > 20 or len(password) < 6:
        message.showinfo("Error", "Password must be between 3 and 20 characters")
        return
    
    mycursor.execute("SELECT * FROM user WHERE username = %s", (username,))
    result = mycursor.fetchall()
    if len(result) > 0:
        message.showinfo("Error", "Username already exists")
    else:
        mycursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password))
        mydb.commit()
        message.showinfo("Success", "User successfully added")
        register_frame.destroy()
        create_login()

def registerUser():
    login_frame.destroy()
    global register_frame
    
    register_frame = Frame(window, width=500, height=400)
    register_frame.grid(row=1, column=0, sticky="NW")
    register_frame.grid_propagate(0)
    register_frame.update()
    
    username_label = Label(register_frame, text="Enter Username: ")
    username_label.place(x=250, y=10, anchor="center")
    username = Entry(register_frame, width=20)
    username.place(x=250, y=30, anchor="center")
    
    password_label = Label(register_frame, text="Enter Password: ")
    password_label.place(x=250, y=60, anchor="center")
    password = Entry(register_frame, width=20, show="*")
    password.place(x=250, y=80, anchor="center")
    
    back = Button(register_frame, text="Back", command=lambda: create_login())
    back.place(x=225, y=110, anchor="center")
    register = Button(register_frame, text="Register", command=lambda: addUser(username.get(), password.get()))
    register.place(x=275, y=110, anchor="center")
    
#Creates initial window
def create_window():
    global window
    global title
    global title_frame

    window = tk.Tk()
    window.title("GPA Calculator")
    window.geometry("500x250")

    f = Frame(window,width=500,height=60)
    f.grid(row=0,column=0,sticky="NW")
    f.grid_propagate(0)
    f.update()
    l = Label(f,text="GPA Calculator", font=("Arial", 28, "bold"), fg="blue")
    l.place(x=250, y=25, anchor="center")

def create_login():
    global login_frame
    login_frame = Frame(window, width=500, height=400)
    login_frame.grid(row=1, column=0, sticky="NW")
    login_frame.grid_propagate(0)
    login_frame.update()
    
    username_label = Label(login_frame, text="Username: ")
    username_label.place(x=250, y=10, anchor="center")
    username = Entry(login_frame, width=20)
    username.place(x=250, y=30, anchor="center")
    
    password_label = Label(login_frame, text="Password: ")
    password_label.place(x=250, y=60, anchor="center")
    password = Entry(login_frame, width=20, show="*")
    password.place(x=250, y=80, anchor="center")
    
    login = Button(login_frame, text="Login", command=lambda: loginCheck(username.get(), password.get()))
    login.place(x=225, y=110, anchor="center")
    
    register = Button(login_frame, text="Register", command=registerUser)
    register.place(x=275, y=110, anchor="center")
    
    authorinfo = Label(login_frame, text="Created by: Zachary Averbach", font=("Arial", 8, "italic"), fg="blue")
    authorinfo.place(x=250, y=140, anchor="center")
create_window()
#create_login()
gpaCalculator("regal72")
window.mainloop()