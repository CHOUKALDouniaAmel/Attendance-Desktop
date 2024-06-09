import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd

class ViewClassAttendance:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("View Class Attendance")
        self.window.geometry("600x400")
        
        records = pd.read_csv('class_list.csv')
        
        for idx, student in records.iterrows():
            tk.Label(self.window, text=student['Name']).grid(row=idx, column=0)
            tk.Label(self.window, text=student['Attendance']).grid(row=idx, column=1)
