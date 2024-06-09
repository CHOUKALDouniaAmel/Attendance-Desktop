import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd

class AttendanceSummary:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Attendance Summary Report")
        self.window.geometry("600x400")
        
        self.summary_button = tk.Button(self.window, text="Generate Summary", command=self.generate_summary)
        self.summary_button.pack(pady=20)
        
        self.summary_text = tk.Text(self.window)
        self.summary_text.pack(pady=20)
        
    def generate_summary(self):
        records = pd.read_csv('class_list.csv')
        total_students = len(records)
        present_count = len(records[records['Attendance'] == 'Present'])
        absent_count = len(records[records['Attendance'] == 'Absent'])
        late_count = len(records[records['Attendance'] == 'Late'])
        
        summary = (
            f"Total Students: {total_students}\n"
            f"Present: {present_count}\n"
            f"Absent: {absent_count}\n"
            f"Late: {late_count}\n"
        )
        
        self.summary_text.delete(1.0, tk.END)
        self.summary_text.insert(tk.END, summary)
