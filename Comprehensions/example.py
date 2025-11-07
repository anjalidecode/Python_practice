# List comprehension
square = [x**2 for x in range(1, 6)]

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}

# Set comprehension
unique_chars = {char for char in "hello"}

print("List comprehension:", square)
print("Dictionary comprehension:", squares)
print("Set comprehension:", unique_chars)
