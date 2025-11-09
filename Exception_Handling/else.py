try:
    result = 5 / 2
except ZeroDivisionError:
    print("Caught and handled error")
else:
    print("No exception occurred")
finally:
    print("End of the try-except-else block")
    
