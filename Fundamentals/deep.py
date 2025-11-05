import copy

list1 = [[1, 2, 3], [4, 5, 6]]
list2 = copy.deepcopy(list1)  # Deep copy

print("Before change:")
print("list1:", list1)
print("list2:", list2)

list2[0][0] = 99  # Change nested element
print("\nAfter change:")
print("list1:", list1)  # list1 is safe
print("list2:", list2)

#A deep copy creates a new object and recursively copies all nested objects.
#So, any change in one copy does not affect the other.