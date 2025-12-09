# "Duck Typing" = Another way to achieve polymorphism besides inheritance
#                 Object must have the minimum necessary attributes/methods
#                 "If it looks like a duck and quacks like a duck, it must be a duck."


class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

d = Dog()
c = Cat()

d.speak()
c.speak()