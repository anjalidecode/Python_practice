# __init__() method is called automatically every time the class is being used to create a new object.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

d1 = Dog("Buddy", 3)
d1.bark()