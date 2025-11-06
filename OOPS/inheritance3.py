# Defining parents classes
class ChefChinese:
    def make_noodles(self):
        print("Making Chinese style noodles")

class ChefItalian:
    def make_pasta(self):
        print("Making Italian style pasta")

# Defining derived class with multiple inheritance
class ChefVersatile(ChefChinese, ChefItalian):
    pass

# Creating an object 
chef_versatile = ChefVersatile()

# Accessing inherited methods
chef_versatile.make_noodles()
chef_versatile.make_pasta()
     