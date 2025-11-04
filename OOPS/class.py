# Define a class called 'Pesron'
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# create object (instances) of a Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Access attributes and call methos on the objects
print(person1.age)
print(person2.name)
person1.introduce()
person2.introduce()