import curses

def ui(stdscr):
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