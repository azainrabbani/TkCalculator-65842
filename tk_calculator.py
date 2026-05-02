import tkinter as tk
from tkinter import messagebox
import math

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

def square():
    try:
        value = float(num1.get())
        result = value ** 2
        output.set(result)
    except:
        messagebox.showerror("Error", "Invalid Input!")

def square_root():
    try:
        value = float(num1.get())
        if value < 0:
            messagebox.showwarning("Warning", "Cannot find square root of negative number!")
        else:
            result = math.sqrt(value)
            output.set(result)
    except:
        messagebox.showerror("Error", "Invalid Input!")

def clear():
    num1.set("")
    num2.set("")
    output.set("")

# -------- GUI Setup --------

root = tk.Tk()
root.title("Tkinter Calculator")
root.geometry("320x350")
root.resizable(False, False)

# Variables
num1 = tk.StringVar()
num2 = tk.StringVar()
output = tk.StringVar()

# -------- UI Elements --------

# Input Fields
tk.Label(root, text="Enter First Number").pack(pady=5)
tk.Entry(root, textvariable=num1).pack()

tk.Label(root, text="Enter Second Number").pack(pady=5)
tk.Entry(root, textvariable=num2).pack()

# Operation Buttons
tk.Button(root, text="Add", width=15, command=add).pack(pady=3)
tk.Button(root, text="Subtract", width=15, command=subtract).pack(pady=3)
tk.Button(root, text="Multiply", width=15, command=multiply).pack(pady=3)
tk.Button(root, text="Divide", width=15, command=divide).pack(pady=3)

# New Features
tk.Button(root, text="Square (Num1)", width=15, command=square).pack(pady=3)
tk.Button(root, text="Square Root (Num1)", width=15, command=square_root).pack(pady=3)

# Result Display
tk.Label(root, text="Result").pack(pady=5)
tk.Entry(root, textvariable=output, state='readonly').pack()

# Clear Button
tk.Button(root, text="Clear", width=15, command=clear).pack(pady=10)

# Run App
root.mainloop()