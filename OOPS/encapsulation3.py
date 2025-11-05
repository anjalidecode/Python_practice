class Secret:
    def __init__(self):
        self.__password = "hidden123"

    def reveal(self, key):
        if key == "admin":
            return self.__password
        else:
            return "Access Denied!"

obj = Secret()
print(obj.reveal("user"))   # Access Denied
print(obj.reveal("admin"))  # hidden123
# print(obj.__password)  Not allowed
print(obj._Secret__password)  # Possible, but bad practice
