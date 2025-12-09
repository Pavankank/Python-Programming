import tkinter
from tkinter import ttk
import random
import time

window = tkinter.Tk()
window.geometry("600x600")
window.title("Pavan's window")
counter = 0 

while counter < 100:
    colors = ["blue","red","yellow","green","pink","purple","light green","orange","light blue"]
    random.shuffle(colors)

    frame1 = tkinter.Frame(window, width=200, height=200, bg=colors[0])
    frame2 = tkinter.Frame(window, width=200, height=200, bg=colors[1])
    frame3 = tkinter.Frame(window, width=200, height=200, bg=colors[2])
    frame4 = tkinter.Frame(window, width=200, height=200, bg=colors[3])
    frame5 = tkinter.Frame(window, width=200, height=200, bg=colors[4])
    frame6 = tkinter.Frame(window, width=200, height=200, bg=colors[5])
    frame7 = tkinter.Frame(window, width=200, height=200, bg=colors[6])
    frame8 = tkinter.Frame(window, width=200, height=200, bg=colors[7])
    frame9 = tkinter.Frame(window, width=200, height=200, bg=colors[8])

    frame1.grid(row=0,column=0)
    frame2.grid(row=0,column=1)
    frame3.grid(row=0,column=2)
    frame4.grid(row=1,column=0)
    frame5.grid(row=1,column=1)
    frame6.grid(row=1,column=2)
    frame7.grid(row=2,column=0)
    frame8.grid(row=2,column=1)
    frame9.grid(row=2,column=2)

    counter +=1
    time.sleep(1)
    
    window.mainloop()
            