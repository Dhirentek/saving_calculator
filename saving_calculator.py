
import tkinter
import tkinter.messagebox
from tkinter import Tk,Label,Entry,Button,END,LEFT,RIGHT
from tkinter import *

import math

root = Tk()

l1=Label(root,text="Enter per day saving amount: ").pack()
e1=Entry(root,bd=10)
e1.pack()

l2=Label(root,text="How Many Years you want to Save ? : ").pack()
e2=Entry(root,bd=10)
e2.pack()


root.geometry("600x400")
root.title("Saving Calculator By DMT H4CK3R")
root.configure(bg='SeaGreen1')


def cal():
   
    a=int(e1.get())
    b=int(e2.get())
    month = a*30
    months = month*6
    year = month*12
    iyear = year*b
    l1=Label(root,text=('Monthly: ',int(month),'Rs'),fg='red',font=("Helvetica", 25)).pack()
    l2=Label(root,text=('6 months: ',int(months),'Rs'),fg='red',font=("Helvetica", 25)).pack()
    l3=Label(root,text=('yearly: ',int(year),'Rs'),fg='red',font=("Helvetica", 25)).pack()
    l4=Label(root,text=(b,'year: ',int(iyear),'Rs'),fg='red',font=("Helvetica", 25)).pack()
   
	

def clear1():
    e1.delete(0,END)

def clear2():
    e2.delete(0,END)
    
def ex():
    root.withdraw()
    
b1=Button(root,text='Calculate',command=cal,bg='SeaGreen3',height=2,width=10)
b1.pack()

b2=Button(root,text='Clear-1',command=clear1,bg='SeaGreen3',height=2,width=10)
b2.pack(side=LEFT)

b3=Button(root,text='Clear-2',command=clear2,bg='SeaGreen3',height=2,width=10)
b3.pack(side=RIGHT)

b3=Button(root,text='Exit',command=ex,bg='SeaGreen3',height=2,width=10)
b3.pack(side=BOTTOM)

root.mainloop()

