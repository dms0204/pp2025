import tkinter as tk
from domains.student_mark_system import StudentMarkSystem
from output import MainUI

if __name__ == "__main__":
    system = StudentMarkSystem()
    root = tk.Tk()
    MainUI(root, system)
    root.mainloop()