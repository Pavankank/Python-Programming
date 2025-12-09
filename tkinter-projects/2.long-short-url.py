import tkinter
import pyshorteners

# Constants
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 250

class LongShort:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        self.window.title("URL Shortener")

        self.frame = tkinter.Frame(self.window)

        self.create_widgets()
        self.place_widgets()

    def create_widgets(self):
        self.title_label = tkinter.Label(self.frame,text = "URL Shortener", font=("",15, "bold"))
        self.long_url_label = tkinter.Label(self.frame,text="Enter Long URL")
        self.short_url_label = tkinter.Label(self.frame,text="Shortened URL")
        self.long_url_entry = tkinter.Entry(self.frame)
        self.short_url_entry = tkinter.Entry(self.frame)
        self.output_button = tkinter.Button(self.frame, text="Enter", font=("",13,"bold"), fg="Blue", command=self.shorten)
        self.frame.pack()

    def place_widgets(self):
        self.title_label.grid(row=0, column=1)
        self.long_url_label.grid(row=1, column=0, pady=20)
        self.short_url_label.grid(row=2, column=0)
        self.long_url_entry.grid(row=1, column=1)
        self.short_url_entry.grid(row=2, column=1)
        self.output_button.grid(row=1, column=2)

    def shorten(self):
        self.short_url_entry.delete(first=0,last=1000)
        self.shortener = pyshorteners.Shortener()
        self.short_url = self.shortener.tinyurl.short(self.long_url_entry.get())
        self.short_url_entry.insert(0, self.short_url)

    def run(self):
        self.window.mainloop()
        
if __name__ == "__main__":
    win = LongShort()
    win.run()

