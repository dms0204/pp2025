import tkinter as tk

class MainUI:
    def __init__(self, root, system):
        self.system = system
        self.root = root
        root.title("Student Mark System (PW9)")
        root.geometry("400x300")

        tk.Label(root, text="Student Mark System", font=("Arial", 16)).pack(pady=10)

        tk.Button(root, text="Input students", width=25,
                  command=lambda: system.input_students()).pack(pady=5)
        tk.Button(root, text="Input courses", width=25,
                  command=lambda: system.input_courses()).pack(pady=5)
        tk.Button(root, text="Input marks", width=25,
                  command=lambda: system.input_marks()).pack(pady=5)
        tk.Button(root, text="Show GPA (desc)", width=25,
                  command=lambda: system.show_gpa()).pack(pady=5)

        tk.Button(root, text="Quit", width=25, command=root.quit).pack(pady=10)