# Abstraction means hiding complex implementation details and showing only the essential features to the user.

from abc import ABC, abstractclassmethod #ABC(Abstract Base Class) from abc module

class Animal(ABC):

    @abstractclassmethod
    def speak(self):
        pass
 
 # subclass1
class Dog(Animal):

    def speak(self):
        return "Woof!"
    
# subclass2
class Cat(Animal):

    def speak(self):
        return "Meow!"
    
#animal = Animal() # This will raise an error, as Animal is an abstract class  — can't create object of abstract class
dog = Dog()
print(dog.speak())
cat = Cat()
print(cat.speak())