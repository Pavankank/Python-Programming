import tkinter as tk
from tkinter import ttk
import openpyxl

class PyExcel:
    def __init__(self):
        self.root = tk.Tk()
        self.style = ttk.Style(self.root)
        self.root.tk.call("source", "/Users/kankanala/Documents/Python-Programming/tkinter-projects/11.pythonexcelapp/forest-light.tcl")
        self.root.tk.call("source", "/Users/kankanala/Documents/Python-Programming/tkinter-projects/11.pythonexcelapp/forest-dark.tcl")
        self.style.theme_use("forest-light")
        self.combo_list = ["Subscribed", "Not Subscribed", "Other"]
        self.emp = tk.StringVar(value="Employed")

        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        self.create_frames()
        self.create_widgets()
        self.place_widgets()
        self.create_tree()

    def create_frames(self):
        self.widgets_frame = ttk.LabelFrame(self.frame, text="Insert Row")
        self.widgets_frame.grid(row=0, column=0, padx=20, pady=10)
        self.treeFrame = ttk.Frame(self.frame)
        self.treeFrame.grid(row=0, column=1, padx=20, pady=10)

    def create_tree(self):
        self.treeScroll = ttk.Scrollbar(self.treeFrame)
        self.treeScroll.pack(side="right", fill="y")
        self.cols = ("Name", "Age", "Subscription", "Employment")
        self.treeview = ttk.Treeview(self.treeFrame, show="headings", yscrollcommand=self.treeScroll.set, columns=self.cols, height=13)
        self.treeview.column("Name", width=100)
        self.treeview.column("Age", width=50)
        self.treeview.column("Subscription", width=100)
        self.treeview.column("Employment", width=100)
        self.treeScroll.config(command=self.treeview.yview)
        self.load_data()

    def create_widgets(self):
        self.name_entry = ttk.Entry(self.widgets_frame)
        self.age_spinbox = ttk.Spinbox(self.widgets_frame, from_=18, to=100)
        self.status_combobox = ttk.Combobox(self.widgets_frame, values=self.combo_list)
        self.employement = ttk.Checkbutton(self.widgets_frame, text="Employed", variable=self.emp, onvalue="Employed", offvalue="Unemployed")
        self.submit_button = ttk.Button(self.widgets_frame, text="Submit", command=self.submit_data)
        self.seperator = ttk.Separator(self.widgets_frame)
        self.dark_mode_switch = ttk.Checkbutton(self.widgets_frame, text="Dark Mode", style="Switch", command=self.toggle_mode)

    def place_widgets(self):
        self.name_entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.name_entry.insert(0, "Name")
        self.name_entry.bind("<FocusIn>", lambda e: self.name_entry.delete('0', 'end'))
        self.age_spinbox.grid(row=1, column=0, padx=5, pady=5,sticky="ew")
        self.age_spinbox.insert(0, "Age")
        self.status_combobox.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        self.status_combobox.current(0)
        self.employement.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        self.submit_button.grid(row=4, column=0, padx=5, pady=5, sticky="ew")
        self.seperator.grid(row=5, column=0, padx=(20,10), pady=10, sticky="ew")
        self.dark_mode_switch.grid(row=6, column=0, padx=5, pady=5, sticky="nsew")

    def load_data(self):
        self.path = "/Users/kankanala/Documents/Python-Programming/tkinter-projects/11.pythonexcelapp/people.xlsx"
        self.workbook = openpyxl.load_workbook(self.path)
        self.sheet = self.workbook.active

        self.list_values = list(self.sheet.values)
        for col_name in self.list_values[0]:
            self.treeview.heading(col_name, text=col_name)

        for value_tuple in self.list_values[1:]:
            self.treeview.insert('', tk.END, values=value_tuple)

    def submit_data(self):
        pass

    def toggle_mode(self):
        if self.dark_mode_switch.instate(["selected"]):
            self.style.theme_use("forest-dark")
        else:
            self.style.theme_use("forest-light")
        
    def run(self):
        self.treeview.pack()
        self.root.mainloop()

if __name__ == "__main__":
    root = PyExcel()
    root.run()


