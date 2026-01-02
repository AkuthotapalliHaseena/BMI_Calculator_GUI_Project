import tkinter as tk
from tkinter import messagebox
import webbrowser

from model.bmi_model import BMIModel
from service.bmi_service import BMIService
from utils.bmi_utils import BMIUtils


class BMIGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("350x300")
        self.root.resizable(False, False)

        tk.Label(root, text="BMI Calculator", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(root, text="Weight (kg):").pack()
        self.weight_entry = tk.Entry(root)
        self.weight_entry.pack()

        tk.Label(root, text="Height (m):").pack()
        self.height_entry = tk.Entry(root)
        self.height_entry.pack()

        tk.Button(root, text="Calculate BMI", command=self.calculate_bmi).pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=5)

        tk.Button(root, text="Open Health Tips", command=self.open_health_page).pack(pady=5)

    def calculate_bmi(self):
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

            BMIUtils.validate_input(weight, height)

            model = BMIModel(weight, height)
            service = BMIService()

            bmi = service.calculate_bmi(model.weight, model.height)
            category = service.get_bmi_category(bmi)

            self.result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def open_health_page(self):
        webbrowser.open("https://www.who.int/news-room/fact-sheets/detail/obesity-and-overweight")
