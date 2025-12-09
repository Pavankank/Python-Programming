# https://www.youtube.com/watch?v=MeMCBdnhvQs&list=PLs3IFJPw3G9IiHm9PEP1UaMtuvACmxVMj

# Importing module
import tkinter  
from tkinter import messagebox

# Window size and configuration
window = tkinter.Tk()
window.title("Login Form")
window.geometry('340x440')
window.configure(bg='#333333')

def login():
    username = "pavan"
    password = "12345"
    if username_entry.get() == username and password_entry.get() == password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")
frame = tkinter.Frame(bg='#333333')

# Creating widgets
login_label = tkinter.Label(frame, text="Login", bg='#333333', fg='Light Blue', font=("Arial", 30))
username_label = tkinter.Label(frame, text = "Username", font=("Arial", 16, "bold"), bg='#333333', fg = '#FFFFFF')
username_entry = tkinter.Entry(frame, font=("Arial", 16))
password_label = tkinter.Label(frame, text = "Password", font=("Arial", 16, "bold"), bg='#333333', fg = '#FFFFFF')
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
login_button = tkinter.Button(frame, text="Login", font=("Arial", 16, "bold"), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news",pady=10)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady = 10)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=10)

frame.pack()
window.mainloop()

