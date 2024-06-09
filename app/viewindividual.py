import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd

class ViewIndividualAttendance:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("View Individual Attendance")
        self.window.geometry("600x400")

        tk.Label(self.window, text="Enter Student Name").pack(pady=10)
        self.student_entry = tk.Entry(self.window)
        self.student_entry.pack(pady=10)

        self.search_button = tk.Button(self.window, text="Search", command=self.search_student)
        self.search_button.pack(pady=10)

        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack(pady=20)

    def search_student(self):
        student_name = self.student_entry.get()
        records = pd.read_csv('class_list.csv')
        student_record = records[records['Name'] == student_name]
        if not student_record.empty:
            attendance_status = student_record['Attendance'].values[0]
            self.result_label.config(text=f"Attendance: {attendance_status}")
        else:
            self.result_label.config(text="Student not found")
