from docxtpl import DocxTemplate
import os, random, datetime
from datetime import date

doc_template_path = "/Users/kankanala/Documents/Python-Programming/tkinter-projects/8.invoice-generator/invoice_template.docx"

invoice_list = [[2,"Pen",0.5,1],[4,"Pencil",1,4]]
first_name = "Pavan"
last_name = "Kankanala"
today = date.today()


if not os.path.isfile(doc_template_path):
    print(f"Error: File '{doc_template_path}' not found.")
else:
    doc = DocxTemplate(doc_template_path)
    doc.render({"name": f"{first_name} {last_name}", 
                "invoice_list": invoice_list,
                "invoice_num": random.randint(10000,20000),
                "today_date": today.strftime("%m/%d/%Y")})
    doc.save(f"/Users/kankanala/Documents/Python-Programming/tkinter-projects/8.invoice-generator/{first_name}_{last_name}_invoice.docx")
    print("Invoice generated successfully.")
