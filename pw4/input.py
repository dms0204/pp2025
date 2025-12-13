import math
from .domains.student import Student
from .domains.course import Course

def input_students(system):
    s = int(input("Enter number of students: "))
    for i in range(s):
        print("Student", i + 1)
        system.students.append(Student.input())

def input_courses(system):
    c = int(input("Enter number of courses: "))
    for j in range(c):
        print("Course:", j + 1)
        system.courses.append(Course.input())

def input_marks(system):
    course_id = input("Enter course ID to input mark: ")
    if course_id not in system.marks:
        system.marks[course_id] = {}

    for std in system.students:
        s_id = std.get_Std_id()
        s_name = std.get_Std_name()
        initial_mark = float(input(f"Mark for {s_name} ({s_id}): "))
        rounded_mark = math.floor(initial_mark * 10) / 10.0
        system.marks[course_id][s_id] = rounded_mark