def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e1:
        raise ValueError("Cannot divide by zero ") from e1
    
try:
    divide(10, 0)
except ValueError as e2:
    print(f"Caught an exception: {e2}")
    print(f"Original exception: {e2.__cause__}")

        
