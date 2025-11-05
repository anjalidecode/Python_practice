class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a noise.")

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        super().speak()
        print(f"{self.name} the {self.breed} says meow meow!")

cat = Cat("Kitty", "Persian")
cat.speak()
        