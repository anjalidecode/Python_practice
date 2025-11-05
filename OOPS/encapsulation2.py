class Person:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age    # private attribute

    # getter method
    def get_age(self):
        return self.__age

    # setter method
    def set_age(self, age):
        if 0 < age < 120:
            self.__age = age
        else:
            print("Invalid age entered!")

    def show(self):
        print(f"Name: {self.__name}, Age: {self.__age}")


# create object
p1 = Person("Alice", 21)
p1.show()

# use setter method to modify private variable
p1.set_age(25)
print("Updated Age:", p1.get_age())

# invalid input (will trigger validation)
p1.set_age(-5)
