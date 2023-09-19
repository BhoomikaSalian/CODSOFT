import tkinter as tk

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        result_label.config(text="Task added successfully")
    else:
        result_label.config(text="Task cannot be empty")

def remove_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        task_listbox.delete(index)
        tasks.pop(index)
        result_label.config(text="Task removed successfully")
    else:
        result_label.config(text="Select a task to remove")

def clear_tasks():
    task_listbox.delete(0, tk.END)
    tasks.clear()
    result_label.config(text="All tasks cleared")

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, font=("Arial", 14))
entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task, width=10)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task, width=10)
remove_button.pack()

clear_button = tk.Button(root, text="Clear All", command=clear_tasks, width=10)
clear_button.pack()

task_listbox = tk.Listbox(root, font=("Arial", 14), selectmode=tk.SINGLE)
task_listbox.pack()

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

root.mainloop()
