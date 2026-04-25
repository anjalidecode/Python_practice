# Hiding internal details and showing only necessary functionality.

from abc import ABC, abstractmethod

class Vehicle(ABC):   # Abstract class
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with key")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with kick")

# object creation
c = Car()
b = Bike()

c.start()
b.start()