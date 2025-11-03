class Calculator:
    def add(self, num1, num2):
        result = num1 + num2
        return result
    
my_calculator = Calculator()
sum_result = my_calculator.add(5, 6)
print(f"The sum of 5 and 6 is {sum_result}.")
