from distutils.cmd import Command
import tkinter as tk
from tkinter import ttk
import datetime as dt
root = tk.Tk()
root.geometry("400x400")
root.title("MUKESH")
root.configure(bg="light blue")
d_student = {'Hari':'12345','Mukesh':'punda','Akarsh':'glasses','Maneesh':'pooka','Chaturya':'Bday','Akkshitha':'Spine'}
d_staff = {'Siva':'god','Assistant':'veruppu','Jayakanth':'Sivabrother','Shiny':'leftus'}
d_admin = {'Tarun Kumar Singh':'Weed'}


def std():
    student=tk.Tk()
    student.geometry("400x200")
    student.title("STUDENT LOGIN")
    user_n=tk.StringVar()
    pass_n=tk.StringVar()
    l1 = tk.Label(student,text="USERNAME",bg="red").place(x=50,y=0)
    l2 = tk.Label(student,text="PASSWORD",bg="GREEN").place(x=50,y=50)
    e1 = tk.Entry(student,width="10",textvariable=user_n)
    e1.place(x=200,y=0)
    e2 = tk.Entry(student,width="10",textvariable=pass_n)
    e2.place(x=200,y=50)
    user_n=e1.get()
    pass_n=e2.get()
    
    if(d_student[user_n] and d_student[user_n]==pass_n):
        
        s1.config(command=studentpage)
        def studentpage():
            stupa=tk.Tk()
            stupa.geometry("400x200")
            stupa.title("STUDENT PAGE")

    else:
        s1.config(command=errorpage)
        def errorpage():
            error=tk.Tk()
            error.geometry("400x200")
            error.title("ValueError")
            l1=tk.Label(student,text="USERNAME/PASSWORD IS INCORRECT!!!",bg="red")
            l1.pack()
    
    
    s1 = tk.Button(student,text="login",bg="blue",command=studentpage)
    s1.place(x=200,y=100)
    student.mainloop()

o2=tk.Button(root,text="Student",command=std,width="10").place(x=170,y=200)



root.mainloop()