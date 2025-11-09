try:

    result = 1 / 0
    my_list = [1, 2, 3]
    print(my_list[3])

except(ZeroDivisionError, IndexError) as e:
    print(f"Caught an exception: {e}")
