# Defining a base class Vehicle
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def honk(self):
        print(f"{self.make} {self.model} says honk honk")

# inheriting from Vehicle class to create a car
class Car(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year) # Call Vehicle.__init__()
        self.color = color

    def honk(self):
        print(f"{self.color} { self.make} {self.model} says honk honk! I am a car!.")

car1 = Car("Toyota", "Carmy", 2020, "Blue")
car2 = Car("Honda", "Civic", 2019, "Red")

# Accessing object properties and methods
print(car1.make, car1.model, car1.year, car1.color)
car1.honk()
car2.honk()




        