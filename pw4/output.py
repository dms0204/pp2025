import curses
from .input import input_students, input_courses, input_marks

def ui(stdscr, system):
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Student Mark System (curses)")
        stdscr.addstr(2, 0, "1. Input students")
        stdscr.addstr(3, 0, "2. Input courses")
        stdscr.addstr(4, 0, "3. Input marks")
        stdscr.addstr(5, 0, "4. Show GPA(by desc)")
        stdscr.addstr(6, 0, "q. Quit")
        stdscr.addstr(8, 0, "Choose: ")
        stdscr.refresh()

        key = stdscr.getkey().lower()
        if key == "q":
            break

        curses.endwin()

        if key == "1":
            input_students(system)
        elif key == "2":
            input_courses(system)
        elif key == "3":
            input_marks(system)
        elif key == "4":
            system.sort_students_by_gpa()
            print("\nGPA list(by desc):")
            for s in system.students:
                sid = s.get_Std_id()
                print(f"{s.get_Std_name()} ({sid}) GPA={system.calculate_gpa(sid)}")
        else:
            print("Invalid choice!\n")

        input("\nPress Enter to return to menu...")