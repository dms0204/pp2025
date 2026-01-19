import math
from domains.student import Student
from domains.course import Course

def input_students(system):
    s = int(input("Enter numbers of students: "))
    for i in range(s):
        print(f"Student {i+1}")
        std = Student()
        std.input()
        system.students.append(std)

    with open("students.txt", "w", encoding="utf-8") as f:
        for s in system.students:
            f.write(f"{s.get_Std_id()},{s.get_Std_name()},{s.get_Std_DoB()}\n")

def input_courses(system):
    c = int(input("Enter numbers of courses: "))
    for j in range(c):
        print(f"Course {j+1}")
        cr= Course()
        cr.input()
        system.courses.append(cr)

    with open("courses.txt", "w", encoding="utf-8") as f:
        for c in system.courses:
            f.write(f"{c.get_C_id()},{c.get_C_name()},{c.get_Credit()}\n")

def input_marks(system):
    for course in system.courses:
        course_id = course.get_C_id()
        print(f"\nEnter marks for course {course_id}")
        system.marks[course_id] = {}

        for std in system.students:
            mark = float(input(f"Mark for {std.get_Std_name()} ({std.get_Std_id()}): "))
            mark = math.floor(mark * 10)/10
            system.marks[course_id][std.get_Std_id()] = mark

        with open("marks.txt", "w", encoding="utf-8") as f:
            for cid in system.marks:
                for sid, mark in system.marks[cid].items():
                    f.write(f"{cid},{sid},{mark}\n")