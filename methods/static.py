class Calculator:
    @staticmethod #decorator
    def add(a,b):
        return a + b
    
    @staticmethod
    def multiply(a,b):
        return a * b

#Calling static methods on the class itself rather than the instance of the class.
#self parameter is not required , it cannot modify the state of an instance or class

result1 = Calculator.add(10, 20)
result2 = Calculator.multiply(5, 8)
print(result1, result2)
