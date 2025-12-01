students = []
courses = []
marks = {}
def input_students():
    n = int(input("Enter numbers of students: "))
    for i in range(n):
        std_id = input("Enter student ID: ")
        std_name = input("Enter student name: ")
        std_DoB = input("Enter student DoB: ")
        student = {"id": std_id, "name": std_name, "DoB": std_DoB}
        students.append(student)

def input_courses():
    n = int(input("Enter numbers of courses: "))
    for j in range(n):
        c_id = input("Enter course ID: ")
        c_name = input("Enter course name: ")
        course = {"id": c_id, "name": c_name}
        courses.append(course)

def input_marks():
    n = int(input("Enter number of marks: "))
    for k in range(n):
        m_id = input("Enter mark ID: ")
        m_name = input("Enter mark name: ")
        m_student = input