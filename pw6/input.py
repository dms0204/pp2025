import math
from domains.student import Student
from domains.course import Course
import pickle
import gzip

def input_students(system):
    s = int(input("Enter numbers of students: "))
    for i in range(s):
        print(f"Student {i+1}")
        std = Student()
        std.input()
        system.students.append(std)

    with gzip.open("students.dat", "wb") as f:
        pickle.dump(system.students, f)

def input_courses(system):
    c = int(input("Enter numbers of courses: "))
    for j in range(c):
        print(f"Course {j+1}")
        cr = Course()
        cr.input()
        system.courses.append(cr)

    with gzip.open("courses.dat", "wb") as f:
        pickle.dump(system.courses, f)

def input_marks(system):
    for course in system.courses:
        course_id = course.get_C_id()
        print(f"\nEnter marks for course {course_id}")
        system.marks[course_id] = {}

        for std in system.students:
            mark = float(input(f"Mark for {std.get_Std_name()} ({std.get_Std_id()}): "))
            mark = math.floor(mark * 10)/10
            system.marks[course_id][std.get_Std_id()] = mark

        with gzip.open("marks.dat", "wb") as f:
            pickle.dump(system.marks, f)