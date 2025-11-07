def uppercase_decorator(function):
    def wrapper():
        func = function()
        uppercase_func = func.upper()
        return uppercase_func
    
    return wrapper

@uppercase_decorator
def greet():
    return "Helllo World!"

print(greet())