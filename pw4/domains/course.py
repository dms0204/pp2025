class Course:
    count2 = 0
    
    def __init__(self, c_id, c_name, c_credit):
        Course.count2 +=1
        self.index2 = Course.count2
        self.__id = c_id
        self.__name = c_name
        self.__credit = c_credit
    #getter
    def get_C_id(self):
        return self.__id
    def get_C_name(self):
        return self.__name
    def get_C_credit(self):
        return self.__credit
    #polymorphism
    def input():
        c_id = input("Enter course ID: ")
        c_name = input("Enter course name: ")
        c_credit = int(input("Enter course credits: "))
        return Course(c_id, c_name, c_credit)
    
    def __str__(self):
        return f"Course {self.index2}: {self.__id}, {self.__name}"