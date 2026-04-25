# It refers to methods/functions/operators with the same name that can be executed on many objects or classes.

class Cat:
    def sound(self):
        print("Meow")

class Fox:
    def sound(self):
        print("Wa-pa-pa-pa-pa-pow!")

c1 = Cat() 
f1 = Fox()

# duck typing uses different objects in the same way because they share the same method.

for x in (c1, f1):
    x.sound()