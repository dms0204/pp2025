from .entity import Entity
class Course(Entity):
    count2 = 0

    # Constructor
    def __init__(self, c_id = "", c_name = "", credit = 0):
        Course.count2 += 1
        self.index2 = Course.count2
        self.__id = c_id
        self.__name = c_name
        self.__credit = credit
    
    # Polymorphism
    def input(self):
        self.__id = input("Enter course ID: ")
        self.__name = input("Enter course name: ")
        self.__credit = int(input("Enter course credit: "))
    # Getter
    def get_C_id(self):
        return self.__id
    def get_C_name(self):
        return self.__name
    def get_Credit(self):
        return self.__credit
    
    # Polymorphism
    def list(self):
        return f"Course {self.index2}: {self.__id}, {self.__name}"