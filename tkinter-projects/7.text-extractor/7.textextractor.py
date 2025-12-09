import tkinter, PyPDF2
from tkinter import filedialog, ttk

# Main function for opening file, reading and inserting into the text box
def OpenFile():
    filename = filedialog.askopenfilename(title="Open PDF File", 
                initialdir='/Users/kankanala/Documents/Python-Programming/tkinter-projects/7.text-extractor',
                filetypes=[('PDF files', '*.pdf')])
    
    filename_label.configure(text=filename)
    outputfile_text.delete("1.0", tkinter.END)
    reader = PyPDF2.PdfReader(filename)
    for page in reader.pages:
        current_text = page.extract_text()
        outputfile_text.insert(tkinter.END, current_text)

# Window creation
window = tkinter.Tk()
window.title("PDF Text Extractor")

# Window labels & Button creation
filename_label = ttk.Label(window, text="No File Selected")
outputfile_text = tkinter.Text(window)
filename_button = ttk.Button(window, text="Open PDF File", command=OpenFile)

# Lables & Button placement
filename_label.pack()
outputfile_text.pack()
filename_button.pack()

window.mainloop()