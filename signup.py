from tkinter import *
cal=Tk()
cal.geometry("1600x720")
cal.title("Sign up")
cal.configure(background="dodgerblue4")
from tkinter import messagebox
def signup():
    pass1=password1.get()
    pass2=password2.get()
    first=firstname.get()
    last=lastname.get()
    e=email.get()
    

    if(pass1 == pass2):
        call=database()
    else:
        messagebox.showerror("ERROR","Please Enter password correctly")


def database():
    pass1=password1.get()
    pass2=password2.get()
    firstn=firstname.get()
    lastn=lastname.get()
    e=email.get()
    val = (firstn, lastn, e, pass1)
    import sqlite3
    conn=sqlite3.connect('admin.db')
    #conn.execute('''create table record(first char(20) not null, last char(20) not null, email char (50) not null, password char(50) not null);''')
    mycursor = conn.cursor()
    mycursor.execute("INSERT INTO record (first, last, email, password) VALUES (?,?,?,?)",val)
    call=login()
def login():
    cal.destroy()
    import login.py

firstname = StringVar()
lastname = StringVar()
email = StringVar()
password1 = StringVar()
password2 = StringVar()







Label(cal,font=('helvetica',50,'bold'),text="CGPA CALCULATOR",bd=10,fg="white",background="Dodgerblue4").place(x=320,y=0)
w=Canvas(cal, width=640, height=400,background="white").place(x=327,y=130)

Label(cal,font=('helvetica',20,'bold'),text="Sign Up",bd=10,fg="black",background="white").place(x=350,y=150)
Label(cal,font=('helvetica',10,'bold'),text="Please fill this form to create account",bd=10,fg="grey",background="white").place(x=350,y=197)
Label(cal,font=('helvetica',13,'bold'),text="First Name",bd=10,fg="Black",background="white").place(x=350,y=230)
Label(cal,font=('helvetica',13,'bold'),text="Last Name",bd=10,fg="black",background="white").place(x=350,y=270)
Label(cal,font=('helvetica',13,'bold'),text="Email",bd=10,fg="black",background="white").place(x=350,y=310)
Label(cal,font=('helvetica',13,'bold'),text="Password",bd=10,fg="black",background="white").place(x=350,y=350)
Label(cal,font=('helvetica',13,'bold'),text="Confirm Password",bd=10,fg="black",background="white").place(x=350,y=390)

e1=Entry(cal, font=('arial', 16),width=20,background="ivory2", textvariable=firstname).place(x=554,y=235)
e2=Entry(cal, font=('arial', 16),width=20,background="ivory2", textvariable=lastname).place(x=554,y=275)
e3=Entry(cal, font=('arial', 16),width=20,background="ivory2", textvariable=email).place(x=554,y=315)
e4=Entry(cal, font=('arial', 16),width=20,background="ivory2",show="*", textvariable=password1).place(x=554,y=355)

e5=Entry(cal, font=('arial', 16, 'bold'),width=20,background="ivory2",show="*", textvariable=password2).place(x=554,y=395)
b1=Button(cal, font=('arial', 16, 'bold'),text="Sign Up",background="Dodgerblue4",fg="white",width=14,cursor="hand2",command=signup).place(x=355,y=440)

