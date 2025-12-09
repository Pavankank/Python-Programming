import tkinter, os, random
from tkinter import ttk, messagebox
from docxtpl import DocxTemplate
from datetime import date
import docx2pdf

class DataEntry:    
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Invoice Generator Form")
        self.frame = ttk.Frame(self.window)
        self.window.configure(background="#ececec")

        self.serial_number = 1
        self.invoice_list = []

        self.create_labels()
        self.place_labels()
        self.create_entrys()
        self.place_entrys()
        self.create_buttons()
        self.place_buttons()
        self.create_tree()
        self.place_tree()

    def create_labels(self):
        self.first_name_label = ttk.Label(self.frame, text="First Name")
        self.last_name_label = ttk.Label(self.frame, text="Last Name")
        self.company_label = ttk.Label(self.frame, text="Company")
        self.phone_label = ttk.Label(self.frame, text="Phone")
        self.description_label = ttk.Label(self.frame, text="Description")
        self.quantity_label = ttk.Label(self.frame, text="Quantity")
        self.unit_price_label = ttk.Label(self.frame, text="Unit Price")

    def create_entrys(self):
        self.first_name_entry = ttk.Entry(self.frame)
        self.last_name_entry = ttk.Entry(self.frame)
        self.company_entry = ttk.Entry(self.frame)
        self.phone_entry = ttk.Entry(self.frame)
        self.description_entry = ttk.Entry(self.frame)
        self.quantity_entry_spinbox = ttk.Spinbox(self.frame, from_=1, to=100)
        self.unit_price_entry = ttk.Entry(self.frame)

    def create_buttons(self):
        self.add_item_button = ttk.Button(self.frame, text="Add item", command=self.add_item)
        self.generate_invoice_button = ttk.Button(self.frame, text="Generate Invoice", command=self.generate_invoice)
        self.new_invoice_button = ttk.Button(self.frame, text="New Invoice", command = self.new_invoice)

    def create_tree(self):
        columns = ('sno','qty', 'desc', 'price','total')
        self.tree = ttk.Treeview(self.frame, columns=columns, show="headings")
        self.tree.heading('sno', text="S.No")
        self.tree.heading('qty', text="Quantity")
        self.tree.heading('desc', text="Description")
        self.tree.heading('price', text="Unit Price")
        self.tree.heading('total', text="Total")

    def place_labels(self):
        self.first_name_label.grid(row=0, column=0, pady=10)
        self.last_name_label.grid(row=0, column=1)
        self.company_label.grid(row=0, column=2)
        self.phone_label.grid(row=0, column=3)
        self.description_label.grid(row=2, column=0, pady=10, columnspan=2)
        self.quantity_label.grid(row=2, column=1, columnspan=2)
        self.unit_price_label.grid(row=2, column=2, columnspan=2)

    def place_entrys(self):
        self.first_name_entry.grid(row=1,column=0,padx=10)
        self.last_name_entry.grid(row=1,column=1,padx=10)
        self.company_entry.grid(row=1,column=2,padx=10)
        self.phone_entry.grid(row=1,column=3,padx=10)
        self.description_entry.grid(row=3,column=0,columnspan=2)
        self.quantity_entry_spinbox.grid(row=3, column=1, columnspan=2)
        self.unit_price_entry.grid(row=3,column=2, columnspan=2)

    def place_buttons(self):
        self.add_item_button.grid(row=4,column=1, sticky="news", pady=20, columnspan=2)
        self.generate_invoice_button.grid(row=6,column=0, sticky="news", pady=10, padx=10, columnspan=2)
        self.new_invoice_button.grid(row=6, column=2, sticky="news", pady=10, padx=10, columnspan=2)
    
    def place_tree(self):
        self.tree.grid(row=5, column=0, columnspan=4, pady=10)
    
    def add_item(self):
        self.first_name = self.first_name_entry.get()
        self.last_name = self.last_name_entry.get()
        self.phone = self.phone_entry.get()
        self.description = self.description_entry.get()
        self.company = self.company_entry.get()
        self.quantity = self.quantity_entry_spinbox.get()
        self.unit_price = self.unit_price_entry.get()

        self.missing_fields = []

        if not self.first_name:
            self.missing_fields.append("First Name")
        if not self.last_name:
            self.missing_fields.append("Last Name")
        if not self.phone:
            self.missing_fields.append("Phone")
        if not self.company:
            self.missing_fields.append("Company")
        if not self.description:
            self.missing_fields.append("Description")
        if not self.quantity:
            self.missing_fields.append("Quantity")
        if not self.unit_price:
            self.missing_fields.append("Unit Price")

        if self.missing_fields:
            messagebox.showwarning(title="Warning", message="The following fields are missing: " + ", ".join(self.missing_fields))
        elif len(self.phone) != 10 or not self.phone.isdigit():
            messagebox.showwarning("Warning", "Entered phone number is incorrect.")
        else:
            try:
                self.quantity = int(self.quantity)
                self.unit_price = float(self.unit_price)
                self.line_total = self.quantity * self.unit_price
                self.invoice_item =[self.serial_number, self.quantity, self.description, self.unit_price, self.line_total]
                self.tree.insert('', 'end', values=self.invoice_item)
                self.serial_number += 1
                self.clear_item()
                self.invoice_list.append(self.invoice_item)
            except ValueError as e:
                messagebox.showerror(title="Error", message=e)

    def clear_item(self):
        self.description_entry.delete(0,tkinter.END)
        self.quantity_entry_spinbox.delete(0,tkinter.END)
        self.unit_price_entry.delete(0,tkinter.END)

    def new_invoice(self):
        self.serial_number = 1
        self.first_name_entry.delete(0,tkinter.END)
        self.last_name_entry.delete(0,tkinter.END)
        self.company_entry.delete(0,tkinter.END)
        self.phone_entry.delete(0,tkinter.END)
        self.tree.delete(*self.tree.get_children())
        self.clear_item()
        self.invoice_list.clear()

    def generate_invoice(self):
        if len(self.invoice_list) != 0:
            self.doc_template_path = "/Users/kankanala/Documents/Python-Programming/tkinter-projects/8.invoice-generator/invoice_template.docx"
            self.today = date.today()
            self.invoice_num=random.randint(10000,20000)
            self.subtotal = sum(self.item[4] for self.item in self.invoice_list)
            self.salestax = self.subtotal * 0.00
            self.total = self.subtotal + self.salestax

            if not os.path.isfile(self.doc_template_path):
                print(f"Error: File '{self.doc_template_path}' not found.")
            else:
                doc = DocxTemplate(self.doc_template_path)
                doc.render({"name": f"{self.first_name} {self.last_name}",
                            "company_name": self.company,
                            "phone_num": self.phone,
                            "invoice_num": self.invoice_num,
                            "today_date": self.today.strftime("%m/%d/%Y"),
                            "invoice_list": self.invoice_list, 
                            "salestax":"$ "+str(round(self.salestax,2)), 
                            "subtotal":"$ "+str(round(self.subtotal,2)), 
                            "total":"$ "+str(round(self.total,2))})
                doc.save(f"/Users/kankanala/Documents/Python-Programming/tkinter-projects/8.invoice-generator/{self.first_name}_{self.last_name}_{self.invoice_num}_invoice.docx")
                messagebox.showinfo(title="Success",message="Invoice generated successfully.")
        else:
            messagebox.showwarning("Warning", "There are no items entered.")

    def run(self):
        self.frame.pack(padx=20, pady=20)
        self.window.mainloop()

if __name__ == "__main__":
    win = DataEntry()
    win.run()