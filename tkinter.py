from tkinter import *
#import tkinter as Tk
window=Tk()
window.title("My Supermarket Billing System")

Label (window,text="Supermarket Billing System",font="none 20 bold",padx=15,pady=15).grid(row=0,column=7,rowspan=2,sticky=W+E+N+S)

Label (window,text="ITEMS",fg="black",font="none 15 bold",padx=10,pady=10).grid(row=2,column=0,sticky=W)
list1=[]
list2=[]
def add():
        list1.append("Soap")
        list2.append(50)
        print(list1)
        print(list2)

def add1():
    list1.append("Detergent")
    list2.append(70)
    print(list1)
    print(list2)

def add2():
    list1.append("Pen")
    list2.append(20)
    print(list1)
    print(list2)
    
def add3():
    list1.append("Bottle")
    list2.append(40)
    print(list1)
    print(list2)

def add4():
    list1.append("Textbook")
    list2.append(200)
    print(list1)
    print(list2)
    
def add5():
    list1.append("Towel")
    list2.append(100)
    print(list1)
    print(list2)    
    
    
Label (window,text="1.Soap           [ Rs. 50  ]",fg="black",font="none 20").grid(row=3,column=0,sticky=W) #soap label
Label (window,text="2.Detergent   [ Rs. 70  ]",fg="black",font="none 20").grid(row=7  ,column=0,sticky=W,columnspan=10) #detergent label
Label (window,text="3.Pen             [ Rs. 20  ]",fg="black",font="none 20").grid(row=11,column=0,sticky=W,columnspan=10) #pen label
Label (window,text="4.Bottle          [ Rs. 40  ]",fg="black",font="none 20").grid(row=15,column=0,sticky=W,columnspan=10) #bottle label
Label (window,text="5.Textbook    [ Rs. 200]",fg="black",font="none 20").grid(row=19,column=0,sticky=W,columnspan=10) #textbook label
Label (window,text="6.Towel          [ Rs. 100]",fg="black",font="none 20").grid(row=23,column=0,sticky=W,columnspan=10) #towel label
#Label(window,text="7.bucket          [ Rs. 145]",fg="black",font="none 20").grid(row=27,column=0,sticky=W,columnspan=10) #bucket label
#Label(window,text="8.Toothbrush  [ Rs. 30  ]",fg="black",font="none 20").grid(row=31,column=0,sticky=W,columnspan=10) #toothbrush label
#Label(window,text="9.file               [ Rs. 10  ]",fg="black",font="none 20").grid(row=35,column=0,sticky=W,columnspan=10) #projectfile label


    
Button(window,text="ADD SOAP",width=9,command=add).grid(row=3,column=7)
Button(window,text="ADD DETERGENT",width=14,command=add1).grid(row=7,column=7)
Button(window,text="ADD PEN",width=8,command=add2).grid(row=11,column=7)
Button(window,text="ADD BOTTLE",width=11,command=add3).grid(row=15,column=7)
Button(window,text="ADD TEXTBHOOK",width=14,command=add4).grid(row=19,column=7)
Button(window,text="ADD TOWEL",width=10,command=add5).grid(row=23,column=7)
#Button(window,text="ADD BUCKET",width=11,command=soap).grid(row=27,column=7)
#Button(window,text="ADD TOOTHBRUSH",width=15,command=soap).grid(row=31,column=7)
#Button(window,text="ADD FILE",width=9,command=soap).grid(row=35,column=7)


window.mainloop()
