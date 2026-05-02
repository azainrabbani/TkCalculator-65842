import tkinter as tk
from tkinter import messagebox


# ----------- BMI Logic -----------
def calculate_bmi():
    try:
        height = float(height_entry.get())
        weight = float(weight_entry.get())

        if height <= 0 or weight <= 0:
            messagebox.showerror("Invalid Input", "Values must be greater than 0")
            return

        bmi = weight / (height ** 2)

        # Classification
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(
            text=f"BMI: {bmi:.2f} ({category})"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values")


# ----------- UI Setup -----------
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x300")
root.resizable(False, False)

# Title
title = tk.Label(root, text="BMI Calculator", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Height Input
height_label = tk.Label(root, text="Height (meters):")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

# Weight Input
weight_label = tk.Label(root, text="Weight (kg):")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

# Calculate Button
calc_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calc_button.pack(pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run App
root.mainloop()