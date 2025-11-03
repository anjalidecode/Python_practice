class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name
    
    def get_salary(self):
        return self.salary
    
    def get_emplpyee_info(self):
        name = self.get_name()
        salary = self.get_salary()
        return f"Name: {name}, Salary: {salary}"
    
employee1 = Employee("Alice", 600000)
employee2= Employee("Carlo",70000)

print(employee1.get_emplpyee_info())
print(employee2.get_emplpyee_info())

        