import copy

list1 = [[1, 2, 3], [4, 5, 6]]
list2 = copy.copy(list1) # shallow copy

print("before changes:")
print("list1:", list1)
print("list2:", list2)

list2[0][0] = 99 # change nested element
print("\nAfter changes:")
print("list1:", list1) #list1 also changes
print("list2:", list2)
