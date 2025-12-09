from tkinter import *

mywin= Tk()

mywin.title("Temperature Converter")
mywin.geometry("300x300")

def convert():
    cel = int(mytextbox.get())
    f = cel * 9/5 + 32
    resultbox.delete(0,END)
    resultbox.insert(0,str(f))

l = Label(mywin, text="Celsius")
l.place(x=5,y=10)

mytextbox = Entry(mywin, width=20)
mytextbox.place(x=70,y=10)

l = Label(mywin, text="Farenheit")
l.place(x=5,y=40)

resultbox = Entry(mywin, width=20)
resultbox.place(x=70,y=40)

b = Button(mywin, text = "CONVERT",command=convert)
b.place(x=70,y=70)

mywin.mainloop()