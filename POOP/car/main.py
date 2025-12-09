from car import Car

car1 = Car("Audi", 2022, "Black", True)
car2 = Car("BMW", 2026, "Red", False)

print(car1.model,car1.year,car1.color,car1.for_sale,Car.axle)
print(car2.model,car2.year,car2.color,car2.for_sale,Car.axle)

print()

car1.start()
car1.drive()
car1.stop()

print()

car2.start()
car2.drive()
car2.stop()

print()

