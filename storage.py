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

#Creates initial window
def create_window():
    global window
    global title
    global title_frame
    
    window = tk.Tk()
    window.title("GPA Calculator")
    window.geometry("500x500")
       
    f = Frame(window,width=500,height=100)
    f.grid(row=0,column=0,sticky="NW")
    f.grid_propagate(0)
    f.update()
    l = Label(f,text="GPA Calculator", font=("Arial", 28, "bold"), fg="blue")
    l.place(x=250, y=25, anchor="center")
    
create_window()
window.mainloop()