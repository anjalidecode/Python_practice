try:
    x = 1 / 0
except ZeroDivisionError:
    print("You can't divide by zero.")
finally:
    print("This line is always excuted.")