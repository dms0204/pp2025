class Student:
    def __init__(self, std_id, std_name, std_DoB):
        self.__id = std_id
        self.__name = std_name
        self.__dob = std_DoB
    #getter
    def get_std_id(self):
        return self.__id
    def get_std_name(self):
        return self.__name
    def get_std_DoB(self):
        return self.__dob
    
    def __str__(self):
        return f"Student[ID: {self.__id}, Name: {self.__name}, DoB: {self.__DoB}]"

class Course:
    def __init__(self, c_id, c_name):
        self.__id = c_id
        self.__name = c_name
    #getter
    def get_c_id(self):
        return self.__id
    def get_c_name(self):
        return self.__name
    
    def __str__(self):
        return f"Course[ID: {self.__id}, Name: {self.__name}]"
    