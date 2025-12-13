import curses
from .domains.mark import StudentMarkSystem
from .output import ui

def main():
    system = StudentMarkSystem()
    curses.wrapper(ui, system)

if __name__ == "__main__":
    main()