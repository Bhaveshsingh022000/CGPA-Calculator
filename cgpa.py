print("WECLOME TO PYTHON GUI")
from tkinter import *
from tkinter import messagebox
cal=Tk()
cal.title("CGPA CALCULATOR")
cal.geometry("1600x720")
cal.configure(background="light goldenrod2")
Label(cal,font=('helvetica',50,'bold'),text="CGPA CALCULATOR",bd=10,fg="white",background="light goldenrod2").place(x=280,y=0)
def helpcal():
    import grade.py

menubar=Menu(cal)
filemenu=Menu(menubar, tearoff=0)
filemenu.add_command(label="Grades",command=helpcal)
menubar.add_cascade(label="Help",menu=filemenu)
cal.config(menu=menubar)

def grade(subgrade):
    if(subgrade==""):
        valsubgrade=0
    elif(subgrade=="O")or(subgrade=="o"):
        valsubgrade=10
    elif(subgrade=="A+")or(subgrade=="a+"):
        valsubgrade=9
    elif(subgrade=="A")or(subgrade=="a"):
        valsubgrade=8
    elif(subgrade=="B+")or(subgrade=="b+"):
        valsubgrade=7
    elif(subgrade=="B")or(subgrade=="b"):
        valsubgrade=6
    elif(subgrade=="C+")or(subgrade=="c+"):
        valsubgrade=5
    elif(subgrade=="C")or(subgrade=="c"):
        valsubgrade=4
    elif(subgrade=="E")or(subgrade=="e"):
        valsubgrade=0
    elif(subgrade=="F")or(subgrade=="f"):
        valsubgrade=0
    elif(subgrade=="G")or(subgrade=="g"):
        valsubgrade=0
    elif(subgrade=="I")or(subgrade=="i"):
        valsubgrade=0
    else:
        messagebox.showerror("ERROR","Please Enter valid Grade")
    return(valsubgrade)

    

def calculate():
    valsub1=grade(sub1.get())
    valsub2=grade(sub2.get())
    valsub3=grade(sub3.get())
    valsub4=grade(sub4.get())
    valsub5=grade(sub5.get())
    valsub6=grade(sub6.get())
    valsub7=grade(sub7.get())
    valsub8=grade(sub8.get())
    valsub9=grade(sub9.get())
    valsub10=grade(sub10.get())
    if(cr1.get()==""):
        valsub1cr1=0
    else:
        valsub1cr1=int(cr1.get())
    if(cr2.get()==""):
        valsub2cr2=0
    else:
        valsub2cr2=int(cr2.get())
    if(cr3.get()==""):
        valsub3cr3=0
    else:
        valsub3cr3=int(cr3.get())
    if(cr4.get()==""):
        valsub4cr4=0
    else:
        valsub4cr4=int(cr4.get())
    if(cr5.get()==""):
        valsub5cr5=0
    else:
        valsub5cr5=int(cr5.get())
    if(cr6.get()==""):
        valsub6cr6=0
    else:
        valsub6cr6=int(cr6.get())
    if(cr7.get()==""):
        valsub7cr7=0
    else:
        valsub7cr7=int(cr7.get())
    if(cr8.get()==""):
        valsub8cr8=0
    else:
        valsub8cr8=int(cr8.get())
    if(cr9.get()==""):
        valsub9cr9=0
    else:
        valsub9cr9=int(cr9.get())
    if(cr10.get()==""):
        valsub10cr10=0
    else:
        valsub10cr10=int(cr10.get())
    
    

    totalsum=valsub1*valsub1cr1+valsub2*valsub2cr2+valsub3*valsub3cr3+valsub4*valsub4cr4+valsub5*valsub5cr5+valsub6*valsub6cr6+valsub7*valsub7cr7+valsub8*valsub8cr8+valsub9*valsub9cr9+valsub10*valsub10cr10
    totalcredit=valsub1cr1+valsub2cr2+valsub3cr3+valsub4cr4+valsub5cr5+valsub6cr6+valsub7cr7+valsub8cr8+valsub9cr9+valsub10cr10
    tgpasem1= '%.2f'%(totalsum/totalcredit)
    tgpa1.set(tgpasem1)

def calculate2():
    valsub11=grade(sub11.get())
    valsub22=grade(sub22.get())
    valsub33=grade(sub33.get())
    valsub44=grade(sub44.get())
    valsub55=grade(sub55.get())
    valsub66=grade(sub66.get())
    valsub77=grade(sub77.get())
    valsub88=grade(sub88.get())
    valsub99=grade(sub99.get())
    valsub101=grade(sub101.get())
    if(cr11.get()==""):
        valsub1cr11=0
    else:
        valsub1cr11=int(cr11.get())
    if(cr22.get()==""):
        valsub2cr22=0
    else:
        valsub2cr22=int(cr22.get())
    if(cr33.get()==""):
        valsub3cr33=0
    else:
        valsub3cr33=int(cr33.get())
    if(cr44.get()==""):
        valsub4cr44=0
    else:
        valsub4cr44=int(cr44.get())
    if(cr55.get()==""):
        valsub5cr55=0
    else:
        valsub5cr55=int(cr55.get())
    if(cr66.get()==""):
        valsub6cr66=0
    else:
        valsub6cr66=int(cr66.get())
    if(cr77.get()==""):
        valsub7cr77=0
    else:
        valsub7cr77=int(cr77.get())
    if(cr88.get()==""):
        valsub8cr88=0
    else:
        valsub8cr88=int(cr88.get())
    if(cr99.get()==""):
        valsub9cr99=0
    else:
        valsub9cr99=int(cr99.get())
    if(cr101.get()==""):
        valsub10cr101=0
    else:
        valsub10cr101=int(cr101.get())
    
    

    totalsum=valsub11*(valsub1cr11)+valsub22*valsub2cr22+valsub33*valsub3cr33+valsub44*valsub4cr44+valsub55*valsub5cr55+valsub66*valsub6cr66+valsub77*valsub7cr77+valsub88*valsub8cr88+valsub99*valsub9cr99+valsub101*valsub10cr101
    totalcredit=valsub1cr11+valsub2cr22+valsub3cr33+valsub4cr44+valsub5cr55+valsub6cr66+valsub7cr77+valsub8cr88+valsub9cr99+valsub10cr101
    tgpasem2= '%.2f'%(totalsum/totalcredit)
    tgpa2.set(tgpasem2)
    
def Reset():
    sub1.set("") 
    sub2.set("")
    sub3.set("")
    sub4.set("")
    sub5.set("")
    sub6.set("")
    sub7.set("")
    sub8.set("")
    sub9.set("")
    sub10.set("")
    cr1.set("")
    cr2.set("")
    cr3.set("")
    cr4.set("")
    cr5.set("")
    cr6.set("")
    cr7.set("")
    cr8.set("")
    cr9.set("")
    cr10.set("")
    tgpa1.set("")

def Reset2():
    sub11.set("") 
    sub22.set("")
    sub33.set("")
    sub44.set("")
    sub55.set("")
    sub66.set("")
    sub77.set("")
    sub88.set("")
    sub99.set("")
    sub101.set("")
    cr11.set("")
    cr22.set("")
    cr33.set("")
    cr44.set("")
    cr55.set("")
    cr66.set("")
    cr77.set("")
    cr88.set("")
    cr99.set("")
    cr101.set("")
    tgpa2.set("")
    
def gpa():
    t1=float(tgpa1.get())
    t2=float(tgpa2.get())
    total='%.2f'%((t1+t2)/2)
    cgpa.set(total)



sub1 = StringVar()
sub2 = StringVar()
sub3 = StringVar()
sub4 = StringVar()
sub5 = StringVar()
sub6 = StringVar()
sub7 = StringVar()
sub8 = StringVar()
sub9 = StringVar()
sub10 = StringVar()

sub11 = StringVar()
sub22 = StringVar()
sub33 = StringVar()
sub44 = StringVar()
sub55 = StringVar()
sub66 = StringVar()
sub77 = StringVar()
sub88 = StringVar()
sub99 = StringVar()
sub101 = StringVar()

cr1 = StringVar()
cr2 = StringVar()
cr3 = StringVar()
cr4 = StringVar()
cr5 = StringVar()
cr6 = StringVar()
cr7 = StringVar()
cr8 = StringVar()
cr9 = StringVar()
cr10 = StringVar()
tgpa1 = StringVar()

cr11 = StringVar()
cr22 = StringVar()
cr33 = StringVar()
cr44 = StringVar()
cr55 = StringVar()
cr66 = StringVar()
cr77 = StringVar()
cr88 = StringVar()
cr99 = StringVar()
cr101 = StringVar()
tgpa2 = StringVar()
cgpa = StringVar()

Label(cal,font=('arial', 16, 'bold'),text="SEMESTER 1",anchor="w",bd=7,fg="black",background="light goldenrod2").place(x=10,y=130)
Label(cal,font=('arial', 16, 'bold'),text="Subject 1",fg="black",background="light goldenrod2").place(x=15,y=190)
Label(cal,font=('arial', 16, 'bold'),text="Subject 2",fg="black",background="light goldenrod2").place(x=15,y=235)
Label(cal,font=('arial', 16, 'bold'),text="Subject 3",fg="black",background="light goldenrod2").place(x=15,y=280)
Label(cal,font=('arial', 16, 'bold'),text="Subject 4",fg="black",background="light goldenrod2").place(x=15,y=325)
Label(cal,font=('arial', 16, 'bold'),text="Subject 5",fg="black",background="light goldenrod2").place(x=15,y=370)
Label(cal,font=('arial', 16, 'bold'),text="Subject 6",fg="black",background="light goldenrod2").place(x=15,y=415)
Label(cal,font=('arial', 16, 'bold'),text="Subject 7",fg="black",background="light goldenrod2").place(x=15,y=460)
Label(cal,font=('arial', 16, 'bold'),text="Subject 8",fg="black",background="light goldenrod2").place(x=15,y=505)
Label(cal,font=('arial', 16, 'bold'),text="Subject 9",fg="black",background="light goldenrod2").place(x=15,y=550)
Label(cal,font=('arial', 16, 'bold'),text="Subject 10",fg="black",background="light goldenrod2").place(x=15,y=595)

Label(cal,font=('arial', 16, 'bold'),text="Grade",background="light goldenrod2",fg="black").place(x=200,y=136)
Label(cal,font=('arial', 16, 'bold'),text="Credit",fg="black",background="light goldenrod2").place(x=300,y=136)
e1=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=sub1).place(x=200,y=190)
f1=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=cr1).place(x=300,y=190)

e2=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=sub2).place(x=200,y=235)
f2=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=cr2).place(x=300,y=235)

e3=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=sub3).place(x=200,y=280)
f3=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=cr3).place(x=300,y=280)

e4=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=sub4).place(x=200,y=325)
f4=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=cr4).place(x=300,y=325)

e5=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=sub5).place(x=200,y=370)
f5=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=cr5).place(x=300,y=370)

e6=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=sub6).place(x=200,y=415)
f6=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=cr6).place(x=300,y=415)

e7=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=sub7).place(x=200,y=460)
f7=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=cr7).place(x=300,y=460)

e8=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=sub8).place(x=200,y=505)
f8=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=cr8).place(x=300,y=505)

e9=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=sub9).place(x=200,y=550)
f9=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=cr9).place(x=300,y=550)

e10=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=sub10).place(x=200,y=595)
f10=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=cr10).place(x=300,y=595)

caltgpa=Button(cal,text='TGPA',font=('arial', 16, 'bold'),background="purple",fg="white", command=calculate).place(x=15,y=640)
tgpasem1=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=tgpa1,bd=5).place(x=200,y=640)
reset1=Button(cal, text='RESET',font=('arial', 16, 'bold'),background="purple",fg="white", command=Reset).place(x=310,y=640)

###################################SEM 2######################################

Label(cal,font=('arial', 16, 'bold'),text="SEMESTER 2",anchor="w",bd=7,fg="black",background="light goldenrod2").place(x=860,y=130)

Label(cal,font=('arial', 16, 'bold'),text="Subject 1",fg="black",background="light goldenrod2").place(x=865,y=190)
Label(cal,font=('arial', 16, 'bold'),text="Subject 2",fg="black",background="light goldenrod2").place(x=865,y=235)
Label(cal,font=('arial', 16, 'bold'),text="Subject 3",fg="black",background="light goldenrod2").place(x=865,y=280)
Label(cal,font=('arial', 16, 'bold'),text="Subject 4",fg="black",background="light goldenrod2").place(x=865,y=325)
Label(cal,font=('arial', 16, 'bold'),text="Subject 5",fg="black",background="light goldenrod2").place(x=865,y=370)
Label(cal,font=('arial', 16, 'bold'),text="Subject 6",fg="black",background="light goldenrod2").place(x=865,y=415)
Label(cal,font=('arial', 16, 'bold'),text="Subject 7",fg="black",background="light goldenrod2").place(x=865,y=460)
Label(cal,font=('arial', 16, 'bold'),text="Subject 8",fg="black",background="light goldenrod2").place(x=865,y=505)
Label(cal,font=('arial', 16, 'bold'),text="Subject 9",fg="black",background="light goldenrod2").place(x=865,y=550)
Label(cal,font=('arial', 16, 'bold'),text="Subject 10",fg="black",background="light goldenrod2").place(x=865,y=595)

Label(cal,font=('arial', 16, 'bold'),text="Grade",background="light goldenrod2",fg="black").place(x=1050,y=136)
Label(cal,font=('arial', 16, 'bold'),text="Credit",fg="black",background="light goldenrod2").place(x=1150,y=136)

e11=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=sub11).place(x=1050,y=190)
f11=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=cr11).place(x=1150,y=190)

e22=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=sub22).place(x=1050,y=235)
f22=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=cr22).place(x=1150,y=235)

e33=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=sub33).place(x=1050,y=280)
f33=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=cr33).place(x=1150,y=280)

e44=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=sub44).place(x=1050,y=325)
f44=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=cr44).place(x=1150,y=325)

e55=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=sub55).place(x=1050,y=370)
f55=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=cr55).place(x=1150,y=370)

e66=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=sub66).place(x=1050,y=415)
f66=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=cr66).place(x=1150,y=415)

e77=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=sub77).place(x=1050,y=460)
f77=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=cr77).place(x=1150,y=460)

e88=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=sub88).place(x=1050,y=505)
f88=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=cr88).place(x=1150,y=505)

e99=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=sub99).place(x=1050,y=550)
f99=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=cr99).place(x=1150,y=550)

e101=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=sub101).place(x=1050,y=595)
f101=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=cr101).place(x=1150,y=595)

caltgpa2=Button(cal,text='TGPA',font=('arial', 16, 'bold'),background="purple",fg="white", command=calculate2).place(x=865,y=640)
tgpasem2=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=tgpa2,bd=5).place(x=1050,y=640)
reset2=Button(cal, text='RESET',font=('arial', 16, 'bold'),background="purple",fg="white", command=Reset2).place(x=1150,y=640)


c1=Entry(cal,font=('arial', 16, 'bold'),width=8, textvariable=cgpa,bd=6).place(x=585,y=640)

b1=Button(cal, font=('arial', 16, 'bold'),text="CGPA",background="purple",fg="white",command=gpa).place(x=600,y=595)
def logout():
    cal.destroy()
    import login.py

ex=Button(cal, font=('arial', 16, 'bold'),text="Logout",background="purple",fg="white",command=logout).place(x=1240,y=10)
    
