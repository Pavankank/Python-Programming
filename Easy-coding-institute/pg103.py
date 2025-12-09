from tkinter import *

win = Tk()

win.title("MyApp")
win.geometry("500x500")

def display():
    Label(win, text=t.get())

l = Label(win,text = "Hello")
l.pack()

t = Entry(win, width=30)
t.pack()

b = Button(win, text = "PRINT", command=display)
b.pack()

win.mainloop()
