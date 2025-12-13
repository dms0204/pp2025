import math
import numpy as np
import curses

class Student:
    count1 = 0

    def __init__(self, std_id, std_name, std_DoB): #constructor
        Student.count1+=1
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
    def get_C_credits(self):
        return self.__credit
    #polymorphism
    def input():
        c_id = input("Enter course ID: ")
        c_name = input("Enter course name: ")
        c_credit = int(input("Enter course credits: "))
        return Course(c_id, c_name, c_credit)
    
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
            #round-down to 1 digit
            initial_mark = float(input(f"Mark for {s_name} ({s_id}): "))
            rounded_mark = math.floor(initial_mark * 10)/10.0

            self.marks[course_id][s_id] = rounded_mark
    
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

    def calculate_gpa(self, s_id):
        credits_list = []
        marks_list = []

        for c in self.courses:
            c_id = c.get_C_id()
            if c_id in self.marks and s_id in self.marks[c_id]:
                credits_list.append(c.get_C_credits())
                marks_list.append(self.marks[c_id][s_id])

        credits_arr = np.array(credits_list)
        marks_arr = np.array(marks_list)

        gpa = np.sum(credits_arr * marks_arr) / np.sum(credits_arr)
        return float(f"{gpa:.2f}")
    
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
            stdscr.addstr(6, 0, "5. q.Quit")
            stdscr.addstr(8, 0, "Choose: ")
            stdscr.refresh()
            key = stdscr.getkey().lower()

            if key == "q":
                break
            
            curses.endwin()
            if key == "1":
                self.input_students()
            elif key == "2":
                self.input_courses()
            elif key == "3":
                self.input_marks()
            elif key == "4":
                self.sort_students_by_gpa()
                print("\nGPA list(by desc):")
                for s in self.students:
                    sid = s.get_Std_id()
                    print(f"{s.get_Std_name()} ({sid}) GPA={self.calculate_gpa(sid)}")
            else:
                print("Invalid choice!\n")
            
            input("\nPress Enter to return to menu...")
    def main(self):
        curses.wrapper(self.ui)


system = StudentMarkSystem()
system.main()