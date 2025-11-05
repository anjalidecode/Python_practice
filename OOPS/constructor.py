class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def display_employee(self):
        print(f"Employee: {self.name}, Salary: {self.salary}, Department: {self.department}.")

emp1 = Employee("Bob", 50000, "HR")

# Using method of the class to display the employee information
emp1.display_employee()
        