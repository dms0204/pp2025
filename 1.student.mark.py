students = []
courses = []
marks = {}

def input_students():
    s = int(input("Enter numbers of students: "))
    for i in range(s):  
        print(f"Student {i+1}")
        std_id = input("Enter student ID: ")
        std_name = input("Enter student name: ")
        std_DoB = input("Enter student DoB: ")
        student = {"id": std_id, "name": std_name, "DoB": std_DoB}
        students.append(student)

def input_courses():
    c = int(input("Enter numbers of courses: "))
    for j in range(c):
        print(f"Course {j+1}")
        c_id = input("Enter course ID: ")
        c_name = input("Enter course name: ")
        course = {"id": c_id, "name": c_name}
        courses.append(course)

def input_marks():
    course_id = input("Enter course ID to input mark: ")
    if course_id not in marks:
        marks[course_id] = {}
    for k in students:
        mark = float(input(f"Enter mark for {k['name']}({k['id']}): "))
        marks[course_id][k["id"]] = mark

def list_students():
    print("\n List students: ")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['DoB']}")

def list_courses():
    print("\n List courses: ")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")

def show_student_marks():
    course_id = input("Enter course ID to show marks: ")
    if course_id not in marks:
        print("No mark for this course")
        return
    print("\n Student marks: ")
    for s in students:
        s_id = s["id"]
        if s_id in marks[course_id]:
            print(f"{s['name']} ({s_id}): {marks[course_id][s_id]}")
        else:
            print(f"{s['name']} ({s_id}): No mark")
def main():
    input_students()
    input_courses()
    input_marks()
    list_students()
    list_courses()
    show_student_marks()

main()