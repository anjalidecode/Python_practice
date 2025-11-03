class Vehical:
    def start_engine(self):
        print("Generic engine starting sounds")

class Car(Vehical):
    def start_engine(self):
        print("Car engine starting with a roar")

class Motorcycle(Vehical):
    def start_engine(self):
        print("Motorcycle engine staring with a vroom")

generic_vehicle = Vehical()
my_car = Car()
my_motorcycle = Motorcycle()

#calling the start_engine method on each object
generic_vehicle.start_engine()
my_car.start_engine()
my_motorcycle.start_engine()

