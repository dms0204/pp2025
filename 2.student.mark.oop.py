class Student:
    count1 = 0

    def __init__(self, std_id, std_name, std_DoB): #constructor
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
    
class Course:
    count2 = 0
    
    def __init__(self, c_id, c_name):
        Course.count2 +=1
        self.index2 = Course.count2
        self.__id = c_id
        self.__name = c_name
    #getter
    def get_C_id(self):
        return self.__id
    def get_C_name(self):
        return self.__name
    #polymorphism
    def input():
        c_id = input("Enter course ID: ")
        c_name = input("Enter course name: ")
        return Course(c_id, c_name)
    
    def __str__(self):
        return f"Course {self.index2}: {self.__id}, {self.__name}"

class StudentMarkSystem():
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}
    
    def input_students(self):
        s = int(input("Enter number of students: "))
        for i in range(s):
            print("Student", i+1)
            self.students.append(Student.input()) #Create a new object and append -> self.students

    def input_courses(self):
        c = int(input("Enter number of courses: "))
        for j in range(c):
            print("Course:", j+1)
            self.courses.append(Course.input())
    
    def input_marks(self):
        course_id = input("Enter course ID to input mark: ")
        if course_id not in self.marks:
            self.marks[course_id] = {}
        for std in self.students:
            s_id = std.get_Std_id()
            s_name = std.get_Std_name()
            m = float(input(f"Mark for {s_name} ({s_id}): "))
            self.marks[course_id][s_id] = m
    
    def list_students(self):
        print("\n List students: ")
        for s in self.students:
            print(s) 

    def list_courses(self):
        print("\n List courses: ")
        for c in self.courses:
            print(c)

    def show_marks(self):
        course_id = input("Enter course ID to input mark: ")
        if course_id not in self.marks:
            print("No mark for this course: ")
            return
        print("\n Student mark: ")
        for s in self.students:
            s_id = s.get_Std_id()
            s_name = s.get_Std_name()
            mark = self.marks[course_id].get(s_id, "No mark")
            print(f"{s_name} ({s_id}): {mark}")

    def main(self):
        self.input_students()
        self.input_courses()
        self.input_marks()
        self.list_students()
        self.list_courses()
        self.show_marks()

system = StudentMarkSystem()
system.main()