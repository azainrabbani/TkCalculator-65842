import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Task Manager")
        self.root.geometry("400x420")

        self.create_widgets()

    def create_widgets(self):
        self.task_input = tk.Entry(self.root, font=("Calibri", 12))
        self.task_input.pack(pady=10)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Add", width=10, command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Delete", width=10, command=self.delete_task).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Clear All", width=10, command=self.clear_all).grid(row=0, column=2, padx=5)

        self.task_list = tk.Listbox(self.root, height=15, width=45)
        self.task_list.pack(pady=10)

        # Double-click to delete
        self.task_list.bind("<Double-Button-1>", lambda e: self.delete_task())

    def add_task(self):
        task = self.task_input.get().strip()
        if task:
            self.task_list.insert(tk.END, task)
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty")

    def delete_task(self):
        try:
            index = self.task_list.curselection()[0]
            self.task_list.delete(index)
        except:
            messagebox.showwarning("Selection Error", "Select a task first")

    def clear_all(self):
        if messagebox.askyesno("Confirm", "Delete all tasks?"):
            self.task_list.delete(0, tk.END)

# Run app
root = tk.Tk()
app = TodoApp(root)
root.mainloop()