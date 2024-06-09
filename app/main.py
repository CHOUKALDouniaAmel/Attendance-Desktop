import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd

from classe import ClassListCreation
from attendance import AttendanceCategories
from record import RecordAttendance
from viewindividual import ViewIndividualAttendance
from viewclass import ViewClassAttendance
from summary import AttendanceSummary



class AttendanceManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Manager")
        self.root.geometry("800x600")

        # Create buttons for navigation
        self.class_list_button = tk.Button(root, text="Class List Creation", command=self.open_class_list_creation)
        self.class_list_button.pack(pady=10)

        self.attendance_categories_button = tk.Button(root, text="Custom Attendance Categories", command=self.open_attendance_categories)
        self.attendance_categories_button.pack(pady=10)

        self.record_attendance_button = tk.Button(root, text="Record Attendance", command=self.open_record_attendance)
        self.record_attendance_button.pack(pady=10)

        self.view_individual_attendance_button = tk.Button(root, text="View Individual Attendance", command=self.open_view_individual_attendance)
        self.view_individual_attendance_button.pack(pady=10)

        self.view_class_attendance_button = tk.Button(root, text="View Class Attendance", command=self.open_view_class_attendance)
        self.view_class_attendance_button.pack(pady=10)

        self.attendance_summary_button = tk.Button(root, text="Attendance Summary Report", command=self.open_attendance_summary)
        self.attendance_summary_button.pack(pady=10)

    def open_class_list_creation(self):
        ClassListCreation(self.root)

    def open_attendance_categories(self):
        AttendanceCategories(self.root)

    def open_record_attendance(self):
        RecordAttendance(self.root)

    def open_view_individual_attendance(self):
        ViewIndividualAttendance(self.root)

    def open_view_class_attendance(self):
        ViewClassAttendance(self.root)

    def open_attendance_summary(self):
        AttendanceSummary(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceManager(root)
    root.mainloop()
