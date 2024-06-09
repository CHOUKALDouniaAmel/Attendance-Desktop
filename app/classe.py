import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd

class ClassListCreation:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Class List Creation")
        self.window.geometry("600x400")

        self.import_button = tk.Button(self.window, text="Import Class List", command=self.import_class_list)
        self.import_button.pack(pady=20)

    def import_class_list(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
        if file_path:
            self.class_list = pd.read_excel(file_path)
            self.class_list['Attendance'] = "Not Marked"
            self.class_list.to_csv('class_list.csv', index=False)
            messagebox.showinfo("Success", "Class list imported successfully!")
