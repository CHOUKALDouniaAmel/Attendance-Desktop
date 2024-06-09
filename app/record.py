import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd

class RecordAttendance:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Record Attendance")
        self.window.geometry("600x400")
        
        # Read the class list from CSV
        self.class_list = pd.read_csv('class_list.csv')

        # Label and entry for session name
        tk.Label(self.window, text="Enter Session Name:").pack(pady=10)
        self.session_entry = tk.Entry(self.window)
        self.session_entry.pack(pady=10)

        # Frame to hold the attendance recording interface
        self.attendance_frame = tk.Frame(self.window)
        self.attendance_frame.pack(pady=20)

        # Create labels and buttons for each student
        for idx, student in self.class_list.iterrows():
            student_name = student['Name']
            tk.Label(self.attendance_frame, text=student_name).grid(row=idx, column=0, padx=10, pady=5)
            tk.Button(self.attendance_frame, text="Present", command=lambda i=idx: self.update_attendance(i, "Present")).grid(row=idx, column=1, padx=10, pady=5)
            tk.Button(self.attendance_frame, text="Absent", command=lambda i=idx: self.update_attendance(i, "Absent")).grid(row=idx, column=2, padx=10, pady=5)
            tk.Button(self.attendance_frame, text="Late", command=lambda i=idx: self.update_attendance(i, "Late")).grid(row=idx, column=3, padx=10, pady=5)

    def update_attendance(self, index, status):
        # Update the attendance status for the selected student
        self.class_list.at[index, 'Attendance'] = status
        self.class_list.to_csv('class_list.csv', index=False)
        messagebox.showinfo("Attendance Recorded", f"Attendance for {self.class_list.at[index, 'Name']} marked as {status}.")



