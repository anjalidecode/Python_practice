class Car:
    def __init__(self, brand, model, price):
        self.brand = brand          # Public
        self._model = model         # Protected
        self.__price = price        # Private

    # Public method
    def show_details(self):
        print(f"Brand: {self.brand}, Model: {self._model}")

    # Protected method
    def _show_model(self):
        print("Protected Method - Model:", self._model)

    # Private method
    def __show_price(self):
        print("Private Method - Price:", self.__price)

    # Public method accessing private method
    def get_price(self):
        self.__show_price()


# Create object
c1 = Car("Tesla", "Model X", 8000000)

# Public Access
c1.show_details()
print("Brand:", c1.brand)

# Protected Access (allowed, but not recommended)
c1._show_model()
print("Model:", c1._model)

# Private Access (not directly accessible)
# print(c1.__price)   #  AttributeError
c1.get_price()        #  Access via public method
print("Access via Name Mangling:", c1._Car__price)
