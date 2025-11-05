def add(a, b):
    print(a + b)     # just shows the result

def add_return(a, b):
    return a + b     # sends the result back

x = add(5, 3)        # prints 8
y = add_return(5, 3)  # returns 8
print("x =", x)
print("y =", y)

"""add() prints but does not return → x is None
   add_return() returns → y holds the value 8

Use print() → only for displaying messages or debugging.
Use return → when writing reusable functions that must send back results."""
