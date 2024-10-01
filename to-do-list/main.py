import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog

# Function to create a database and tasks table
def create_db():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
        )
    ''')
    conn.commit()
    conn.close()

# Function to load tasks from the database
def load_tasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, task, completed FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

# Function to add a task to the database
def add_task(task):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task, completed) VALUES (?, ?)", (task, False))
    conn.commit()
    conn.close()

# Function to complete a task in the database
def complete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (True, task_id))
    conn.commit()
    conn.close()

# Function to delete a task from the database
def delete_task(task_id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

# GUI version of the To-Do List
def gui_interface():
    create_db()  # Create the database and table

    window = tk.Tk()
    window.title("Stylish To-Do List App")
    window.geometry("800x850")
    window.configure(bg="#2C3E50")  # Dark blue background

    # Title label
    title_label = tk.Label(window, text="My To-Do List", font=("Helvetica", 24, "bold"), fg="#ECF0F1", bg="#2C3E50")
    title_label.pack(pady=10)

    # Task list box
    task_list = tk.Listbox(window, width=50, height=15, bg="#34495E", fg="#ECF0F1", font=("Helvetica", 12), selectbackground="#3498DB")
    task_list.pack(pady=10)

    # Add Task button
    def add_task_button():
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            add_task(task)
            update_task_list()

    add_button = tk.Button(window, text="Add Task", command=add_task_button, bg="#27AE60", fg="white", font=("Helvetica", 12))
    add_button.pack(pady=5)

    # Complete Task button
    def complete_task_button():
        selected_task = task_list.curselection()
        if selected_task:
            task_index = selected_task[0]
            task_id = load_tasks()[task_index][0]  # Get task ID from the database
            complete_task(task_id)
            update_task_list()

    complete_button = tk.Button(window, text="Complete Task", command=complete_task_button, bg="#2980B9", fg="white", font=("Helvetica", 12))
    complete_button.pack(pady=5)

    # Delete Task button
    def delete_task_button():
        selected_task = task_list.curselection()
        if selected_task:
            task_index = selected_task[0]
            task_id = load_tasks()[task_index][0]  # Get task ID from the database
            delete_task(task_id)
            update_task_list()

    delete_button = tk.Button(window, text="Delete Task", command=delete_task_button, bg="#E74C3C", fg="white", font=("Helvetica", 12))
    delete_button.pack(pady=5)

    def update_task_list():
        task_list.delete(0, tk.END)
        tasks = load_tasks()
        for task in tasks:
            status = "✔️" if task[2] else "❌"
            task_list.insert(tk.END, f"{task[1]} [{status}]")

    update_task_list()
    window.mainloop()

if __name__ == "__main__":
    gui_interface()
