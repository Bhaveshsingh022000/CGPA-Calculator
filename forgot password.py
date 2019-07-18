from tkinter import *
cal=Tk()
cal.geometry("1600x720")
cal.title("Forgot Password")
cal.configure(background="dodgerblue4")
from tkinter import messagebox

email = StringVar()
npass=StringVar()
cpass=StringVar()

def reset():
    e=email.get()
    np=npass.get()
    cp=cpass.get()

    if(e==""):
        messagebox.showerror("Error","Please Enter Email")
    elif(np==""):
        messagebox.showerror("Error","Please Enter password")
    elif(cp==""):
        messagebox.showerror("Error","Please Enter password")
    elif(np==cp):
        call=login()
    else:
        messagebox.showerror("Error","Please Enter Password Correctly")
    
    import sqlite3
    conn=sqlite3.connect('admin.db')
    mycursor = conn.cursor()
    mycursor.execute("INSERT INTO record (first,last,email, password) VALUES ('x','y',?,?,)",val)
        
    
def login():
    cal.destroy()
    import login.py

w=Canvas(cal, width=640, height=400,background="white").place(x=327,y=130)
Label(cal,font=('helvetica',20,'bold'),text="Reset Password",bd=10,fg="black",background="white").place(x=350,y=150)
Label(cal,font=('helvetica',13,'bold'),text="Email",bd=10,fg="Black",background="white").place(x=350,y=230)
#Label(cal,font=('helvetica',13,'bold'),text="Old Password",bd=10,fg="black",background="white").place(x=350,y=270)
Label(cal,font=('helvetica',13,'bold'),text="New Password",bd=10,fg="black",background="white").place(x=350,y=270)
Label(cal,font=('helvetica',13,'bold'),text="Confirm Password",bd=10,fg="black",background="white").place(x=350,y=310)

e1=Entry(cal, font=('arial', 16),width=20,background="ivory2", textvariable=email).place(x=554,y=235)
#e2=Entry(cal, font=('arial', 16),width=20,background="ivory2",show="*", textvariable=opassword).place(x=554,y=275)
e3=Entry(cal, font=('arial', 16),width=20,background="ivory2",show="*", textvariable=npass).place(x=554,y=275)
e4=Entry(cal, font=('arial', 16),width=20,background="ivory2",show="*", textvariable=cpass).place(x=554,y=315)
b1=Button(cal, font=('arial', 16, 'bold'),text="Reset",background="Dodgerblue4",fg="white",width=14,cursor="hand2",command=reset).place(x=355,y=370)

