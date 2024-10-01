import tkinter as tk
from tkinter import messagebox

class SimpleCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")
        self.master.geometry("300x400")
        self.master.configure(bg="#2C3E50")

        # Number input fields
        self.num1_label = tk.Label(master, text="Enter first number:", bg="#2C3E50", fg="#ECF0F1")
        self.num1_label.pack(pady=5)
        self.num1_entry = tk.Entry(master)
        self.num1_entry.pack(pady=5)

        self.num2_label = tk.Label(master, text="Enter second number:", bg="#2C3E50", fg="#ECF0F1")
        self.num2_label.pack(pady=5)
        self.num2_entry = tk.Entry(master)
        self.num2_entry.pack(pady=5)

        # Operation buttons
        self.add_button = tk.Button(master, text="Add", command=lambda: self.calculate("add"), bg="#27AE60", fg="white")
        self.add_button.pack(pady=5)

        self.subtract_button = tk.Button(master, text="Subtract", command=lambda: self.calculate("subtract"), bg="#2980B9", fg="white")
        self.subtract_button.pack(pady=5)

        self.multiply_button = tk.Button(master, text="Multiply", command=lambda: self.calculate("multiply"), bg="#E74C3C", fg="white")
        self.multiply_button.pack(pady=5)

        self.divide_button = tk.Button(master, text="Divide", command=lambda: self.calculate("divide"), bg="#8E44AD", fg="white")
        self.divide_button.pack(pady=5)

        # Result label
        self.result_label = tk.Label(master, text="", font=("Helvetica", 14), bg="#2C3E50", fg="#ECF0F1")
        self.result_label.pack(pady=20)

    def calculate(self, operation):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            
            if operation == "add":
                result = num1 + num2
                self.result_label.config(text=f"Result: {result}")
            elif operation == "subtract":
                result = num1 - num2
                self.result_label.config(text=f"Result: {result}")
            elif operation == "multiply":
                result = num1 * num2
                self.result_label.config(text=f"Result: {result}")
            elif operation == "divide":
                if num2 == 0:
                    raise ValueError("Cannot divide by zero.")
                result = num1 / num2
                self.result_label.config(text=f"Result: {result}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()
