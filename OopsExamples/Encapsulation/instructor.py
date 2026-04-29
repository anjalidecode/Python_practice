class Instructor:
    def __init__(self):
        self.__instructor_name = None
        self.__technology_skill = []
        self.__experience = None
        self.__avg_feedback = None

    # Setters
    def set_instructor_name(self, instructor_name):
        self.__instructor_name = instructor_name

    def set_technology_skill(self, technology_skill): 
        self.__technology_skill = technology_skill

    def set_experience(self, experience):
        self.__experience = experience

    def set_avg_feedback(self, avg_feedback):
        self.__avg_feedback = avg_feedback

    # Getters
    def get_instructor_name(self):
        return self.__instructor_name

    def get_technology_skill(self):
        return self.__technology_skill

    def get_experience(self):
        return self.__experience

    def get_avg_feedback(self):
        return self.__avg_feedback

    # Eligibility check
    def check_eligibility(self):
        if self.__experience > 3:
            if self.__avg_feedback >= 4.5:
                return True
        else:
            if self.__avg_feedback >= 4:
                return True
        return False

    # Course allocation
    def allocate_course(self, technology):
        if self.check_eligibility() and technology in self.__technology_skill:
            return True
        return False
    
inst = Instructor()

inst.set_instructor_name("John")
inst.set_technology_skill(["Python", "Java"])
inst.set_experience(5)
inst.set_avg_feedback(4.6)

# Print outputs clearly
print("Eligibility:", inst.check_eligibility())
print("Course Allocation (Python):", inst.allocate_course("Python"))
print("Course Allocation (C++):", inst.allocate_course("C++"))    