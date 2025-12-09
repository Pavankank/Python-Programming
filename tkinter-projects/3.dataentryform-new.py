import tkinter
from tkinter import ttk, messagebox

class DataEntry:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Data Entry Form")

        self.frame = ttk.Frame(self.window)

        self.create_frames()
        self.place_frames()
        self.create_widgets()
        self.place_widgets()
        self.widget_padding()

    def create_frames(self):
        self.user_info_frame = ttk.LabelFrame(self.frame, text="User Information")
        self.courses_info_frame = ttk.LabelFrame(self.frame, text="Course Information")
        self.terms_frame = ttk.LabelFrame(self.frame, text="Terms & Conditions")

    def place_frames(self):
        self.user_info_frame.grid(row=0, column=0, padx=20, pady=10)
        self.courses_info_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)
        self.terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

    def create_widgets(self):
        # user_info_frame widgets
        self.first_name_label = ttk.Label(self.user_info_frame, text="First Name")
        self.last_name_label = ttk.Label(self.user_info_frame, text="Last Name")
        self.first_name_entry = ttk.Entry(self.user_info_frame)
        self.last_name_entry = ttk.Entry(self.user_info_frame)
        self.title_label = ttk.Label(self.user_info_frame, text="Title")
        self.title_combobox = ttk.Combobox(self.user_info_frame, values=["", "Mr.", "Mrs.", "Ms.", "Dr."])
        self.age_label = ttk.Label(self.user_info_frame, text = "Age")
        self.age_spinbox = ttk.Spinbox(self.user_info_frame, from_=18, to=110)
        self.nationality_label = ttk.Label(self.user_info_frame,text="Nationality")
        self.nationality_combobox = ttk.Combobox(self.user_info_frame, values=["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", 
            "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", 
            "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", 
            "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", 
            "Chad", "Chile", "China", "Colombia", "Comoros", "Congo (Congo-Brazzaville)", "Congo (DRC)", "Costa Rica", "Côte d'Ivoire", 
            "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", 
            "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Ethiopia", "Fiji", "Finland", "France", "Gabon", "Gambia", 
            "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", 
            "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", 
            "Kazakhstan", "Kenya", "Kiribati", "North Korea", "South Korea", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", 
            "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia (FYROM)", "Madagascar", "Malawi", "Malaysia", 
            "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", 
            "Montenegro", "Morocco", "Mozambique", "Myanmar (Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", 
            "Niger", "Nigeria", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", 
            "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", 
            "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", 
            "Sint Maarten (Dutch part)", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Sudan", "Spain", 
            "Sri Lanka", "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", "Syria", "Tajikistan", "Tanzania", "Thailand", 
            "Timor-Leste (East Timor)", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", 
            "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", 
            "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"])        
        
        # courses_frame widgets
        self.registered_label = ttk.Label(self.courses_info_frame, text="Registration Status")
        self.reg_status_var = tkinter.StringVar(value="Not Registered")
        self.registered_check = ttk.Checkbutton(self.courses_info_frame, text="Currently Registered", variable=self.reg_status_var, 
                                                    onvalue="Registered", offvalue="Not Registered")
        self.numcourses_label = ttk.Label(self.courses_info_frame, text="# Courses Completed")
        self.numcourses_spinbox = ttk.Spinbox(self.courses_info_frame, from_=0, to='infinity')
        self.numsemesters_label = ttk.Label(self.courses_info_frame, text="# Semesters")
        self.numsemesters_spinbox = ttk.Spinbox(self.courses_info_frame, from_=0, to='infinity')

        # terms_frame widgets
        self.terms_check_var = tkinter.StringVar(value="Not Accepted")
        self.terms_check = ttk.Checkbutton(self.terms_frame, text = "I accept the terms and conditions.", variable=self.terms_check_var,
                                               onvalue="Accepted", offvalue="Not Accepted")
        # Button widget
        self.save_data_button = ttk.Button(self.frame, text="Enter data",command=self.enter_data)

    def place_widgets(self):
        # user_info_frame widget placements
        self.title_label.grid(row=0, column=0)
        self.title_combobox.grid(row=1,column=0)
        self.first_name_label.grid(row=0, column=1)
        self.first_name_entry.grid(row=1, column=1)
        self.last_name_label.grid(row=0, column=2)
        self.last_name_entry.grid(row=1, column=2)
        self.age_label.grid(row=2, column=0)
        self.age_spinbox.grid(row=3, column=0)
        self.nationality_label.grid(row=2, column=1)
        self.nationality_combobox.grid(row=3,column=1)

        # courses_frame widget placements
        self.registered_label.grid(row=0, column=0, padx=30, pady=5)
        self.registered_check.grid(row=1, column=0, padx=30, pady=5)
        self.numcourses_label.grid(row=0, column=1, padx=10, pady=5)
        self.numcourses_spinbox.grid(row=1, column=1, padx=10, pady=5)
        self.numsemesters_label.grid(row=0, column=2, padx=10, pady=5)
        self.numsemesters_spinbox.grid(row=1, column=2, padx=10, pady=5)

        # terms_frame widget placements
        self.terms_check.grid(row=0, column=0)

        # button widget placement
        self.save_data_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

    def widget_padding(self):
        for self.widget in self.user_info_frame.winfo_children():
            self.widget.grid_configure(padx=10, pady=5)

    def enter_data(self):
        if self.terms_check_var.get() == "Accepted":

            # User info
            self.firstname = self.first_name_entry.get()
            self.lastname = self.last_name_entry.get()

            if self.firstname and self.lastname:
                self.title = self.title_combobox.get()
                self.age = self.age_spinbox.get()
                self.nationality = self.nationality_combobox.get()

                # Course info
                self.numcourses = self.numcourses_spinbox.get()
                self.numsemesters = self.numsemesters_spinbox.get()
                self.registration_status = self.reg_status_var.get()

                print(f"{self.title} {self.firstname} {self.lastname}, Age: {self.age}, Nationality: {self.nationality}")
                print(f"Num of courses registered: {self.numcourses}, Num of semesters: {self.numsemesters}")
                print(f"Courses registered: {self.registration_status}")
            else:
                tkinter.messagebox.showwarning(title="Error", message="First name and Last name are required.")
        else:
            tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms.")

    def run(self):
        self.frame.pack()
        self.window.mainloop()

if __name__ == "__main__":
    win = DataEntry()
    win.run()