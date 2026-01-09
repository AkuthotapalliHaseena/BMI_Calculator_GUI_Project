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

        tk.Label(root, text="BMI Calculator", font=("Arial", 16, "bold")).grid(row=0,column=0,columnspan=4,pady=10)

        tk.Label(root, text="Weight (kg):").grid(row=1,column=0,padx=10,pady=5,sticky="e")
        self.weight_entry = tk.Entry(root,width=10)
        self.weight_entry.grid(row=1,column=1,padx=5,pady=5)

        tk.Label(root, text="Height (cm):").grid(row=1,column=2,padx=10,pady=5,sticky="e")
        self.height_entry = tk.Entry(root,width=10)
        self.height_entry.grid(row=1,column=3,padx=5,pady=5)

        tk.Button(root, text="Calculate BMI",font=("Arial",12,"bold"), command=self.calculate_bmi).grid(row=2,column=0,columnspan=4,pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.grid(row=3,column=0,columnspan=4,pady=5)

        tk.Button(root, text="Open Health Tips", command=self.open_health_page).grid(row=4,column=0,columnspan=4,pady=5)

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
