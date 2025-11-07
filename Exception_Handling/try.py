def divide(a, b):
    try:         # run the code under try
        result = a / b
    
    except ZeroDivisionError: # if an error occurs execute the code under except
        print("Error: You cannot divide by zero!")
        return None
    return result

result1 = divide(10, 5)
print(f"Result 1: {result1}")
result2 = divide(10, 0)
print(f"Result 2: {result2}")

