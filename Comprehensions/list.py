original_list = [1, 2, 3, 4, 5]
even_list = [x for x in original_list if x % 2 == 0]
print(even_list)

original_fruits = ['apple', 'orange', 'apple', 'banana']
fruits_with_apple_slices = [fruit if fruit != 'apple' else 'apple slice' for fruit in original_fruits]
print(fruits_with_apple_slices)