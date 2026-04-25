class Athlete:
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender
        
    # getter method
        
    def get_name(self):
        return self.__name
        
    def get_gender(self):
        return self.__gender
        
    # setter method
    
    def set_name(self, name):
        self.__name = name
        
    def set_gender(self, gender):
        self.__gender = gender
        

    def running(self):
        if self.__gender=="girl":
            print("150mtr running")
        else:
            print("200mtr running")
            
# Creating object for Maria
athlete1 = Athlete("Maria", "girl")

# Make her run
athlete1.running()
                                        