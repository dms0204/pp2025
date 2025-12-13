class Student:
    count1 = 0

    def __init__(self, std_id, std_name, std_DoB): #constructor
        Student.count1 +=1
        self.index1 = Student.count1
        self.__id = std_id
        self.__name = std_name
        self.__DoB = std_DoB
    #getter
    def get_Std_id(self):
        return self.__id
    def get_Std_name(self):
        return self.__name
    def get_Std_DoB(self):
        return self.__DoB
    
    def input():
        std_id = input("Enter student ID: ")
        std_name = input("Enter student name: ")
        std_DoB = input("Enter student DoB: ")
        return Student(std_id, std_name, std_DoB) #call init
    
    def __str__(self): #string representation
        return f"Student {self.index1}: {self.__id}, {self.__name}, {self.__DoB}"