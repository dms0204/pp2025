import math
import numpy as np

class StudentMarkSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def calculate_gpa(self, s_id):
        credits_list = []
        marks_list = []

        for c in self.courses:
            c_id = c.get_C_id()
            if c_id in self.marks and s_id in self.marks[c_id]:
                credits_list.append(c.get_C_credits())
                marks_list.append(self.marks[c_id][s_id])

        credits_arr = np.array(credits_list)
        marks_arr = np.array(marks_list)

        gpa = np.sum(credits_arr * marks_arr) / np.sum(credits_arr)
        return float(f"{gpa:.2f}")

    def get_gpa(self, student):
        return self.calculate_gpa(student.get_Std_id())

    def sort_students_by_gpa(self):
        self.students.sort(key=self.get_gpa, reverse=True)
