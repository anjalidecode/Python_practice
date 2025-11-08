def level_3():
    return 1/0 # This will raise an error

def level_2():
    return level_3()

def level_1():
    try:
        return level_2()
    except ZeroDivisionError:
        print("Caught and handled ZeroDivisionError in level_1")

result = level_1()