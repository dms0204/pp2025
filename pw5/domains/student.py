from .entity import Entity
class Student(Entity):
    count1 = 0

    # Constructor
    def __init__(self, std_id = "", std_name = "", std_DoB = ""):
        Student.count1 += 1
        self.index1 = Student.count1
        self.__id = std_id
        self.__name = std_name
        self.__DoB = std_DoB

    # Polymorphism
    def input(self):
        self.__id = input("Enter student ID: ")
        self.__name = input("Enter student name: ")
        self.__DoB = input("Enter student DoB: ")

    # Getter
    def get_Std_id(self):
        return self.__id
    def get_Std_name(self):
        return self.__name
    def get_Std_DoB(self):
        return self.__DoB
    
    # Polymorphism
    def list(self):
            return f"Student {self.index1}: {self.__id}, {self.__name}, {self.__DoB}"