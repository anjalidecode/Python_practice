# Class is blueprint used to create objects.

class Person:
    def __init__(self, name, age): #always executed when the class is being initiated
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}")

p1 = Person("John", 36) #object p1 of the class

p1.greet()

    