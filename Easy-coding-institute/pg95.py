class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def display(self):
        print(self.real,"+", self.img,"j")

    c1 = Complex(5,3)
    c2 = Complex(7,5)

