class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, num):
        self.value += num
        return self #returning self allows chaining
    
    def subtract(self, num):
        self.value -= num
        return self
    
    def multiply(self, num):
        self.value *= num
        return self
    
    def result(self):
        return self.value

    
my_calculator = Calculator()

final_result = my_calculator.add(5).subtract(2).multiply(3).result()
print(f"The result of the chained operation is {final_result}")

        