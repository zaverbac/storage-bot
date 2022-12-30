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

mycursor = mydb.cursor()

def loginCheck(username, password):
    if username == "" or password == "":
        message.showinfo("Error", "Please enter a username and password")
        return
    
    mycursor.execute("SELECT * FROM user WHERE username = %s AND password = %s", (username, password))
    result = mycursor.fetchall()
    if len(result) > 0:
        message.showinfo("Success", "Login successful")
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
    window.geometry("500x200")

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
    password = Entry(login_frame, width=20)
    password.place(x=250, y=80, anchor="center")
    
    login = Button(login_frame, text="Login", command=lambda: loginCheck(username.get(), password.get()))
    login.place(x=225, y=110, anchor="center")
    
    register = Button(login_frame, text="Register", command=registerUser)
    register.place(x=275, y=110, anchor="center")
    
create_window()
create_login()
window.mainloop()