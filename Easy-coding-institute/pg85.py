class Dog:
    breed = None
    color = None
    height = None

    def insert(self,b,c,h): #self: it refers to current object
        self.breed = b
        self.color = c
        self.height = h
    
    def show(self):
        print(self.breed,self.color,self.height)

# How to create an object

dog1 = Dog()

dog1.insert("pamerian","lightbrown",1.2)

dog1.show()

dog2 = Dog()

dog2.insert("Huskey","White",4)

dog2.show()