import tkinter as tk
from ui.bmi_gui import BMIGUI

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x700")
    root.configure(bg="pink")
    app = BMIGUI(root)
    root.mainloop()
