import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd

class AttendanceCategories:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("Custom Attendance Categories")
        self.window.geometry("600x400")

        tk.Label(self.window, text="Add or Edit Attendance Categories").pack(pady=10)
        self.category_entry = tk.Entry(self.window)
        self.category_entry.pack(pady=10)
        self.add_button = tk.Button(self.window, text="Add Category", command=self.add_category)
        self.add_button.pack(pady=10)

        self.categories = []
        self.categories_listbox = tk.Listbox(self.window)
        self.categories_listbox.pack(pady=10)

    def add_category(self):
        category = self.category_entry.get()
        if category:
            self.categories.append(category)
            self.categories_listbox.insert(tk.END, category)
            self.category_entry.delete(0, tk.END)
