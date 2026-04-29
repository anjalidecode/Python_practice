class Vehicle:
    def __init__(self):
        self.__vehicle_id = None
        self.__vehicle_type = None
        self.__vehicle_cost = None
        self.__premium_amount = None

    # Getter and Setter methods
    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id

    def get_vehicle_id(self):
        return self.__vehicle_id

    def set_vehicle_type(self, vehicle_type):
        self.__vehicle_type = vehicle_type

    def get_vehicle_type(self):
        return self.__vehicle_type

    def set_vehicle_cost(self, vehicle_cost):
        self.__vehicle_cost = vehicle_cost

    def get_vehicle_cost(self):
        return self.__vehicle_cost

    def set_premium_amount(self, premium_amount):
        self.__premium_amount = premium_amount

    def get_premium_amount(self):
        return self.__premium_amount

    # Method to calculate premium
    def calculate_premium(self):
        if self.__vehicle_type == "Two Wheeler":
            self.set_premium_amount(0.02 * self.__vehicle_cost)
        elif self.__vehicle_type == "Four Wheeler":
            self.set_premium_amount(0.06 * self.__vehicle_cost)
        else:
            print("Invalid vehicle type")
            self.set_premium_amount(None)

    # Method to display details
    def display_vehicle_details(self):
        if self.__premium_amount is not None:
            print("Vehicle ID:", self.__vehicle_id)
            print("Vehicle Type:", self.__vehicle_type)
            print("Vehicle Cost:", self.__vehicle_cost)
            print("Premium Amount:", self.__premium_amount)
        else:
            print("Cannot display details due to invalid vehicle type")


# Testing 

v1 = Vehicle()
v1.set_vehicle_id("V101")
v1.set_vehicle_type("Two Wheeler")
v1.set_vehicle_cost(50000)
v1.calculate_premium()
v1.display_vehicle_details()

print("-------------------")

v2 = Vehicle()
v2.set_vehicle_id("V102")
v2.set_vehicle_type("Four Wheeler")
v2.set_vehicle_cost(800000)
v2.calculate_premium()
v2.display_vehicle_details()

print("-------------------")

v3 = Vehicle()
v3.set_vehicle_id("V103")
v3.set_vehicle_type("Truck")  # Invalid case
v3.set_vehicle_cost(70000)
v3.calculate_premium()
v3.display_vehicle_details()