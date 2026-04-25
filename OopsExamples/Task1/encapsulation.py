# Encapsulation is about protecting data inside a class and accesing from outside the class.

class ScoreBoard:
    def __init__(self, score):
        self.__score = score # private property

    def get_score(self): # getter method
        return self.__score
    
s1 = ScoreBoard(0)
print(s1.get_score()) # access private propety
    