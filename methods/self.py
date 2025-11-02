class Employee:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def introduce(self):
        print(f"Hello my name is {self.name} age {self.age} and I work in {self.department} department.")

emp1 = Employee("Dev",39, "IT")
emp2 = Employee("Sara",30,"Finance")

emp1.introduce()
emp2.introduce()
        