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

def initial_inputs():
    if class_var.get() == 0:
        return message.showerror("Invalid Input", "Please enter a valid number")
    
    index = class_var.get()
    
    #Labels for Classes and Grades
    tk.Label(window, text="class").grid(row=0, column=0)
    tk.Label(window, text="grade").grid(row=0, column=1)
    for i in range(index):
        tk.Entry(window).grid(row=i + 1, column=0)
        tk.Entry(window).grid(row=i + 1, column=1)
        
    button.grid_remove()
    class_Label.grid_remove()
    class_entry.grid_remove()
def calculate_gpa():
    return 0


window = tk.Tk()
window.title("GPA Calculator")
class_var = tk.IntVar()

class_Label = tk.Label(window, text="Enter number of classes")
class_Label.grid(row=0, column=0)
class_entry = tk.Entry(window, textvariable=class_var)
class_entry.grid(row=0, column=1)

button = tk.Button(window, text="Submit", command=initial_inputs)
button.grid(row=1, column=0)
window.grid_columnconfigure(0, pad=8)
window.grid_rowconfigure(0, pad=2)

window.mainloop()


mycursor = mydb.cursor()




