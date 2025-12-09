class Car:

    axle = "4 axle"

    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def start(self):
        print(f"You start the {Car.axle} {self.year} {self.color} {self.model}.")

    def drive(self):
        print(f"You drive the {Car.axle} {self.year} {self.color} {self.model}.")
    
    def stop(self):
        print(f"You stop the {Car.axle} {self.year} {self.color} {self.model}.")