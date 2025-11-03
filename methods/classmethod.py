class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    @classmethod #decorator define a class method within a class 
    def get_student_count(cls): # func belongs to class, takes cls as first argument
        return cls.count
    
student1 = Student("Alice")
student2 = Student("Bob")

print(Student.get_student_count())

