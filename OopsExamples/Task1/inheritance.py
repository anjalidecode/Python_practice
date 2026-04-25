# Inheritance allows us to define a class that inherits all the methods and properties from another class.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)

class Dog(Animal):
    pass

d1 = Dog("Rex")

d1.speak()

        