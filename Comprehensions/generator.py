# Generator comprehension
squares_gen_comp = ( x**2 for x in range(10))

# Accessing elements from the generator comprehension
for square in squares_gen_comp:
    print(square, end=' ')