# Define a base(parent) class called Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal."
    
# Define a subclass(child) class Dog that inherits from Animal
class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"
    
#Create an instance of Dog
my_dog = Dog("Buddy")
print(my_dog.name)
print(my_dog.speak())
        