class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)
    
    def __str__(self):
        return f"{self.real}+{self.imag}j"

c1 = ComplexNumber(1, 2)
c2 = ComplexNumber(8, 4)

c3 = c1 + c2
print("Sum of complex numbers:", c3)

        