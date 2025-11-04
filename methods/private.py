class Secret:
    def __init__(self):
        self.__code = "1234"

    def __show_code(self):  # private method
        print(self.__code)

s = Secret()
# s.__show_code()  Error
s._Secret__show_code()  #  Access with name mangling
