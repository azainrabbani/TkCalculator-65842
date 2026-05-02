import tkinter as tk
from tkinter import messagebox

# -------- Functions --------

def add():
    try:
        result = float(num1.get()) + float(num2.get())
        output.set(result)
    except:
        messagebox.showerror("Error", "Invalid Input!")

def subtract():
    try:
        result = float(num1.get()) - float(num2.get())
        output.set(result)
    except:
        messagebox.showerror("Error", "Invalid Input!")

def multiply():
    try:
        result = float(num1.get()) * float(num2.get())
        output.set(result)
    except:
        messagebox.showerror("Error", "Invalid Input!")

def divide():
    try:
        if float(num2.get()) == 0:
            messagebox.showwarning("Warning", "Cannot divide by zero!")
        else:
            result = float(num1.get()) / float(num2.get())
            output.set(result)
    except:
        messagebox.showerror("Error", "Invalid Input!")

# -------- GUI Setup --------

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Variables
num1 = tk.StringVar()
num2 = tk.StringVar()
output = tk.StringVar()

# Labels and Entry Fields
tk.Label(root, text="Enter First Number").pack(pady=5)
tk.Entry(root, textvariable=num1).pack()

tk.Label(root, text="Enter Second Number").pack(pady=5)
tk.Entry(root, textvariable=num2).pack()

# Buttons
tk.Button(root, text="Add", width=10, command=add).pack(pady=3)
tk.Button(root, text="Subtract", width=10, command=subtract).pack(pady=3)
tk.Button(root, text="Multiply", width=10, command=multiply).pack(pady=3)
tk.Button(root, text="Divide", width=10, command=divide).pack(pady=3)

# Result
tk.Label(root, text="Result").pack(pady=5)
tk.Entry(root, textvariable=output, state='readonly').pack()

# Run App
root.mainloop()