import math
import numpy as np
import curses
from input import input_students, input_courses, input_marks
from output import ui

class StudentMarkSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

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

    def run(self, stdscr):
        while True:
            ui(stdscr)
            key = stdscr.getch()

            if key in (ord('q'), ord('Q')):
                break

            curses.def_prog_mode()
            curses.endwin()

            if key == ord("1"):
                input_students(self)
            elif key == ord("2"):
                input_courses(self)
            elif key == ord("3"):
                input_marks(self)
            elif key == ord("4"):
                self.sort_students_by_gpa()
                print("\nGPA list(by desc):")
                for s in self.students:
                    sid = s.get_Std_id()
                    print(f"{s.get_Std_name()} ({sid}) GPA={self.calculate_gpa(sid)}")
            else:
                print("Invalid choice!")

            input("\nPress Enter to return to menu...")

        curses.reset_prog_mode()
        stdscr.refresh()

    def main(self):
        curses.wrapper(self.ui)