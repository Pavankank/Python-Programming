# How to make a calculator

from tkinter import *

calc = Tk()

calc.title("Calculator")
# calc.geometry("200x200")

def button(num):
    first = display.get()
    display.delete(0,END)
    display.insert(0,first+num)

def plus():
    global first
    first = display.get()
    display.delete(0,END)

def equal():
    sec = display.get()
    res = int(first) + int(sec)
    display.delete(0,END)
    display.insert(0,str(res))

def clear():
    display.delete(0,END)

display = Entry(calc, width=20)
display.grid(row = 0, column=0,columnspan=3,padx=10,pady=10)

b1 = Button(calc, text="1", width=10, height=2, command=lambda : button("1"))
b1.grid(row=1,column=0)
b2 = Button(calc, text="2", width=10, height=2, command=lambda : button("2"))
b2.grid(row=1,column=1)
b3 = Button(calc, text="3", width=10, height=2, command=lambda : button("3"))
b3.grid(row=1,column=2)

b4 = Button(calc, text="4", width=10, height=2, command=lambda : button("4"))
b4.grid(row=2,column=0)
b5 = Button(calc, text="5", width=10, height=2, command=lambda : button("5"))
b5.grid(row=2,column=1)
b6 = Button(calc, text="6", width=10, height=2, command=lambda : button("6"))
b6.grid(row=2,column=2)

b7 = Button(calc, text="7", width=10, height=2, command=lambda : button("7"))
b7.grid(row=3,column=0)
b8 = Button(calc, text="8", width=10, height=2, command=lambda : button("8"))
b8.grid(row=3,column=1)
b9 = Button(calc, text="9", width=10, height=2, command=lambda : button("9"))
b9.grid(row=3,column=2)
b0 = Button(calc, text="0", width=10, height=2, command=lambda : button("0"))
b0.grid(row=4,column=0)

bclear = Button(calc, text="CLEAR", width=10, height=2, command=clear)
bclear.grid(row=4,column=1)
bequal = Button(calc, text="=", width=10, height=2,command=equal)
bequal.grid(row=4,column=2)

bplus = Button(calc, text="+", width=10, height=2,command=plus)
bplus.grid(row=5,column=0)
bplus = Button(calc, text="-", width=10, height=2,command=plus)
bplus.grid(row=5,column=1)
bplus = Button(calc, text="*", width=10, height=2,command=plus)
bplus.grid(row=5,column=2)

calc.mainloop()