import tkinter
from tkinter import messagebox

# Constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 250
TITLE_FONT_SIZE = 30
LABEL_FONT_SIZE = 20
BUTTON_FONT_SIZE = 20

usernames = {"pavan":"12345","aadriti":"12345","ishaan":"12345","ramya":"12345"}

class LoginWindow:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        self.window.title("Login Form")
        # self.window.configure(bg='grey')

        self.frame1 = tkinter.Frame(self.window)

        self.create_widgets()
        self.place_widgets()

    def create_widgets(self):
        self.title_label = tkinter.Label(self.frame1, text="User Login Page", fg="Purple", font=("Arial", TITLE_FONT_SIZE))
        self.username_input_label = tkinter.Label(self.frame1,text="Username", fg="Brown", font=("Arial", LABEL_FONT_SIZE))
        self.username_entry = tkinter.Entry(self.frame1,font=("Arial", LABEL_FONT_SIZE))
        self.username_check_button = tkinter.Button(self.frame1,text="User Check", fg='blue', font=("Arial", BUTTON_FONT_SIZE), command=self.username_check)
        self.password_input_label = tkinter.Label(self.frame1,text="Password", fg="Brown", font=("Arial", LABEL_FONT_SIZE))
        self.password_entry = tkinter.Entry(self.frame1,show="*", font=("Arial", LABEL_FONT_SIZE))
        self.login_button = tkinter.Button(self.frame1,text="Login", font=("Arial", BUTTON_FONT_SIZE), command=self.user_login)
        self.output_label = tkinter.Label(self.frame1,text="", font=("Arial", LABEL_FONT_SIZE))

    def place_widgets(self):
        self.title_label.grid(row=0, column=1, sticky="EW", pady=10)
        self.username_input_label.grid(row=1, column=0, padx=10, pady=10)
        self.username_entry.grid(row=1, column=1)
        self.username_check_button.grid(row=1, column=2)
        self.password_input_label.grid(row=2, column=0)
        self.password_entry.grid(row=2, column=1)
        self.login_button.grid(row=3, column=1, pady=10)
        self.output_label.grid(row=4, column=1)

    def username_check(self):
        input_username = self.username_entry.get()
        if len(input_username) == 0:
            self.output_label.config(text="Enter a username!")
        elif input_username in usernames:
            self.output_label.config(text="User exists!")
        else:
            self.output_label.config(text="Username Not Found!")
        self.window.update()

    def user_login(self):
        input_username = self.username_entry.get()
        if input_username in usernames:
            password = usernames.get(input_username)
            if password == self.password_entry.get():
                self.output_label.config(text="Login Successful!")
                messagebox.showinfo("Logged in successfully.","Logged in successfully.")
            else:
                self.output_label.config(text="Wrong Password Entered!")
        else:
            self.output_label.config(text="Username Not Found!")
            messagebox.showerror("User not found.", "User not found.")
        self.window.update()

    def run(self):
        self.frame1.pack()
        self.window.mainloop()

if __name__ == "__main__":
    window = LoginWindow()
    window.run()