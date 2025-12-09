import tkinter as tk
from tkinter import ttk, filedialog, colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter

class ImageModifier:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1500x700")
        self.root.title("Image Editing Tool")
        self.root.config(bg="white")

        self.frames()

    def frames(self):
        self.left_frame = ttk.Frame(self.root, width=200, height=600)
        self.left_frame.pack(side="left", fill="y")

        self.canvas = tk.Canvas(self.root, width=750, height=600)
        self.canvas.pack()

        self.image_button = ttk.Button(self.left_frame, text="Add Image", command=self.add_image)
        self.image_button.pack(padx=20,pady=10)

    def add_image(self):
        global file_path
        file_path=filedialog.askopenfilename(
            initialdir="/Users/kankanala/Documents/Python-Programming/tkinter-projects/9.image-editing-tool"
        )
        self.image = Image.open(file_path)

    def imagetools(self):
        pen_color = "black"
        pen_size = 5
        file_path = ""

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = ImageModifier()
    root.run()



