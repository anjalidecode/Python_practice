# self is used to access properties and methods that belong to the class.

class Car:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print(self.brand)

c1 = Car("Ford")

c1.show()