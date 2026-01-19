class Entity:
    def input(self):
        pass
    def list(self):
        pass

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
    
class Course(Entity):
    count2 = 0

    # Constructor
    def __init__(self, c_id = "", c_name = ""):
        Course.count2 += 1
        self.index2 = Course.count2
        self.__id = c_id
        self.__name = c_name
    
    # Polymorphism
    def input(self):
        self.__id = input("Enter course ID: ")
        self.__name = input("Enter course name: ")

    # Getter
    def get_C_id(self):
        return self.__id
    def get_C_name(self):
        return self.__name
    
    # Polymorphism
    def list(self):
        return f"Course {self.index2}: {self.__id}, {self.__name}"
    
class StudentMarkSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_students(self):
        s = int(input("Enter numbers of students: "))
        for i in range(s):
            print(f"Student {i+1}")
            std = Student()
            std.input()
            self.students.append(std)
    
    def input_courses(self):
        c = int(input("Enter numbers of courses: "))
        for j in range(c):
            print(f"Course {j+1}")
            cr = Course()
            cr.input()
            self.courses.append(cr)

    def input_marks(self):
        course_id = input("Enter course ID to input mark: ")
        self.marks[course_id] = {}
        for std in self.students:
            mark = float(input(f"Mark for {std.get_Std_name()} ({std.get_Std_id()}): "))
            self.marks[course_id][std.get_Std_id()] = mark
    
    def list_students(self):
        print("\nList students: ")
        for s in self.students:
            print(s.list()) # Polymorphism
    
    def list_courses(self):
        print("\nList courses: ")
        for c in self.courses:
            print(c.list()) # Polymorphism

    def show_marks(self):
        course_id = input("Enter course ID to show mark: ")
        if course_id not in self.marks:
            print("No mark for this course")
            return
        
        print("\nStudent marks: ")
        for s in self.students:
            mark = self.marks[course_id].get(s.get_Std_id(), "No mark")
            print(f"{s.get_Std_name()} ({s.get_Std_id()}): {mark}")

    def main(self):
        self.input_students()
        self.input_courses()
        self.input_marks()
        self.list_students()
        self.list_courses()
        self.show_marks()    

system = StudentMarkSystem()
system.main()