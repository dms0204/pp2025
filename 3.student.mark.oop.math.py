import math
import numpy as np
import curses

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
            self.courses.append(c)

    def input_marks(self):
        for course in self.courses:
            course_id = course.get_C_id()
            print(f"\nEnter marks for course {course_id}")
            self.marks[course_id] = {}

            for std in self.students:
                mark = float(input(f"Mark for {std.get_Std_name()} ({std.get_Std_id()}): "))
                mark = math.floor(mark * 10)/10
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

    def calculate_gpa(self, std_id):
        marks = []
        credits = []
        for course in self.courses:
            c_id = course.get_C_id()
            if c_id in self.marks and std_id in self.marks[c_id]:
                marks.append(self.marks[c_id][std_id])
                credits.append(course.get_Credit())
        
        if not marks:
            return 0.0
        
        marks = np.array(marks)
        credits = np.array(credits)
        gpa = np.sum(marks * credits) / np.sum(credits)
        return round(gpa, 2)
    
    def get_gpa(self, student):
        return self.calculate_gpa(student.get_Std_id())
    def sort_students_by_gpa(self):
        self.students.sort(key=self.get_gpa, reverse=True)

    def ui(self, stdscr):
        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "Student Mark System (curses)") #stdscr.addstr(y, x, "text") with y = row, x = column
            stdscr.addstr(2, 0, "1. Input students")
            stdscr.addstr(3, 0, "2. Input courses")
            stdscr.addstr(4, 0, "3. Input marks")
            stdscr.addstr(5, 0, "4. Show GPA(by desc)")
            stdscr.addstr(6, 0, "Q. Quit")
            stdscr.addstr(8, 0, "Choose: ")
            stdscr.refresh()

            key = stdscr.getch()

            if key in (ord('q'), ord('Q')):
                break

            curses.def_prog_mode()
            curses.endwin()

            if key == ord("1"):
                self.input_students()
            elif key == ord("2"):
                self.input_courses()
            elif key == ord("3"):
                self.input_marks()
            elif key == ord("4"):
                self.sort_students_by_gpa()
                print("\nGPA list(by desc):")
                for s in self.students:
                    sid = s.get_Std_id()
                    print(f"{s.get_Std_name()} ({sid}) GPA={self.calculate_gpa(sid)}")
            else:
                print("Invalid choice!\n")
            
            input("\nPress Enter to return to menu...")

        curses.reset_prog_mode()
        stdscr.refresh()

    def main(self):
        curses.wrapper(self.ui)

system = StudentMarkSystem()
system.main()