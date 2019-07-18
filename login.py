from tkinter import *
cal=Tk()
cal.geometry("1600x720")
cal.title("Login")
Label(cal,font=('helvetica',50,'bold'),text="CGPA CALCULATOR",bd=10,fg="white",background="Dodgerblue4").place(x=320,y=0)
cal.configure(background="Dodgerblue4")
from tkinter import messagebox


def skip():
    cal.destroy()
    import cgpa.py

def sign():
    cal.destroy()
    import signup.py

def search():
    
    

    e=email.get()
    p=email.get()
    if(e==""):
        messagebox.showerror("Error","Please enter Email")
    elif(p==""):
        messagebox.showerror("Error","Please enter Email")
    else:
        cal.destroy()
        import cgpa.py
    
        
    em=""
    ps=""
    import sqlite3
    conn=sqlite3.connect('admin.db')
    cursor=conn.execute("select * from record where email =:e and password=:p",{"e":e, "p":p});
    for row in cursor:
        print(row[0])
        print(row[1])
        




email=StringVar()
pass1=StringVar()
  
w=Canvas(cal, width=640, height=400,background="white").place(x=327,y=130)
Label(cal,font=('helvetica',20,'bold'),text="Login ",fg="Black",background="white").place(x=600,y=150)
Label(cal,font=('helvetica',17,'bold'),text="Email ",fg="Black",background="white").place(x=400,y=230)
Label(cal,font=('helvetica',17,'bold'),text="Password ",fg="black",background="white").place(x=400,y=300)
b1=Button(cal, font=('arial', 16, 'bold'),text="Login",background="Dodgerblue4",fg="white",width=17,cursor="hand2",command=search).place(x=403,y=376)
e1=Entry(cal, font=('arial', 16),width=20,background="ivory2", textvariable=email).place(x=580,y=235)
e2=Entry(cal, font=('arial', 16),show="*",width=20,background="ivory2", textvariable=pass1).place(x=580,y=305)
b2=Button(cal, font=('arial', 11),text="Forgot Password ?",background="white",fg="black",width=18,cursor="hand2").place(x=403,y=423)

b3=Button(cal, font=('arial', 12),text="Sign Up",background="white",fg="black",width=12,cursor="hand2",command=sign).place(x=600,y=463)
Label(cal,font=('helvetica',11),text="Dont have a account ?",fg="black",background="white").place(x=590,y=500)

Button(cal,font=('helvetica',10),text="Skip",fg="white",background="Dodgerblue4",width=7,command=skip).place(x=900,y=500)

