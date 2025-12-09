import tkinter as tk
from tkinter import ttk, messagebox
from docxtpl import DocxTemplate
from datetime import date
import os
import random

class DataEntry:    
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Invoice Generator Form")
        self.window.configure(background="#ececec")
        self.frame = ttk.Frame(self.window)
        self.frame.pack(padx=20, pady=20)

        self.serial_number = 1
        self.invoice_list = []

        self.setup_widgets()

    def setup_widgets(self):
        """Creates and places all widgets in a structured way."""
        labels = ["First Name", "Last Name", "Company", "Phone", "Description", "Quantity", "Unit Price"]
        self.entries = {}

        # Create Labels and Entry Fields
        for i, text in enumerate(labels[:4]):
            ttk.Label(self.frame, text=text).grid(row=0, column=i, pady=10)
            self.entries[text] = ttk.Entry(self.frame)
            self.entries[text].grid(row=1, column=i, padx=10)

        for i, text in enumerate(labels[4:]):
            ttk.Label(self.frame, text=text).grid(row=2, column=i, pady=10, columnspan=2)

        self.entries["Description"] = ttk.Entry(self.frame)
        self.entries["Description"].grid(row=3, column=0, columnspan=2)

        self.entries["Quantity"] = ttk.Spinbox(self.frame, from_=1, to=100)
        self.entries["Quantity"].grid(row=3, column=1, columnspan=2)

        self.entries["Unit Price"] = ttk.Entry(self.frame)
        self.entries["Unit Price"].grid(row=3, column=2, columnspan=2)

        # Buttons
        ttk.Button(self.frame, text="Add Item", command=self.add_item).grid(row=4, column=1, pady=20, columnspan=2)
        ttk.Button(self.frame, text="Generate Invoice", command=self.generate_invoice).grid(row=6, column=0, pady=10, padx=10, columnspan=2)
        ttk.Button(self.frame, text="New Invoice", command=self.new_invoice).grid(row=6, column=2, pady=10, padx=10, columnspan=2)

        # Table
        columns = ('S.No', 'Qty', 'Desc', 'Price', 'Total')
        self.tree = ttk.Treeview(self.frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col.lower(), text=col)
        self.tree.grid(row=5, column=0, columnspan=4, pady=10)

    def add_item(self):
        """Validates input, adds item to invoice list, and updates the table."""
        fields = ["First Name", "Last Name", "Company", "Phone", "Description", "Quantity", "Unit Price"]
        values = {field: self.entries[field].get().strip() for field in fields}

        # Check for missing fields
        missing = [field for field in fields if not values[field]]
        if missing:
            messagebox.showwarning("Warning", f"The following fields are missing: {', '.join(missing)}")
            return

        # Validate phone number
        if len(values["Phone"]) != 10 or not values["Phone"].isdigit():
            messagebox.showwarning("Warning", "Entered phone number is incorrect.")
            return

        # Validate Quantity and Unit Price
        try:
            quantity = int(values["Quantity"])
            unit_price = float(values["Unit Price"])
        except ValueError:
            messagebox.showerror("Error", "Quantity must be an integer and Unit Price must be a number.")
            return

        # Add item to tree and list
        total = quantity * unit_price
        item = [self.serial_number, quantity, values["Description"], unit_price, total]
        self.tree.insert('', 'end', values=item)
        self.invoice_list.append(item)
        self.serial_number += 1

        self.clear_item()

    def clear_item(self):
        """Clears the description, quantity, and unit price fields."""
        self.entries["Description"].delete(0, tk.END)
        self.entries["Quantity"].delete(0, tk.END)
        self.entries["Unit Price"].delete(0, tk.END)

    def new_invoice(self):
        """Resets the form for a new invoice."""
        self.serial_number = 1
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.tree.delete(*self.tree.get_children())
        self.invoice_list.clear()

    def generate_invoice(self):
        """Generates an invoice document from the template."""
        if not self.invoice_list:
            messagebox.showwarning("Warning", "No items entered.")
            return

        template_path = os.path.join(os.getcwd(), "invoice_template.docx")
        if not os.path.isfile(template_path):
            messagebox.showerror("Error", "Invoice template not found.")
            return

        today = date.today()
        invoice_num = random.randint(10000, 20000)
        subtotal = sum(item[4] for item in self.invoice_list)
        salestax = subtotal * 0.07
        total = subtotal + salestax

        doc = DocxTemplate(template_path)
        doc.render({
            "name": f"{self.entries['First Name'].get()} {self.entries['Last Name'].get()}",
            "company_name": self.entries["Company"].get(),
            "phone_num": self.entries["Phone"].get(),
            "invoice_num": invoice_num,
            "today_date": today.strftime("%m/%d/%Y"),
            "invoice_list": self.invoice_list,
            "salestax": f"$ {salestax:.2f}",
            "subtotal": f"$ {subtotal:.2f}",
            "total": f"$ {total:.2f}"
        })

        invoice_filename = f"{self.entries['First Name'].get()}_{self.entries['Last Name'].get()}_{invoice_num}_invoice.docx"
        save_path = os.path.join(os.getcwd(), invoice_filename)
        doc.save(save_path)

        messagebox.showinfo("Success", "Invoice generated successfully.")

    def run(self):
        """Runs the main Tkinter event loop."""
        self.window.mainloop()

if __name__ == "__main__":
    DataEntry().run()
