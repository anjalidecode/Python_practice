class pasta:
    def prepare(self, sauce="tomato", additional_ingredient=None):
        if additional_ingredient:
            print(f"Preparing pasta with {sauce} sauce and {additional_ingredient}.")
        else:
            print(f"Preparing pasta with {sauce} sauce.")

#creating a pasta object
my_pasta = pasta()

#method overloading

my_pasta.prepare()
my_pasta.prepare("alfredo")
my_pasta.prepare("pesto", "chicken")
my_pasta.prepare(additional_ingredient="cheese")
