import tasks
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("todoapp")
main_frame = ttk.Frame(root, padding=(3, 3, 12, 12))
main_frame.grid(column=0, row=0, sticky=(N, W, E, S))

ttk.Label(main_frame, text="Task Name:").grid(column=1, row=1, sticky=(W))
task_name = StringVar()
task_name_entry = ttk.Entry(main_frame, width=35, textvariable=task_name)
task_name_entry.grid(column=2, row=1, sticky=(W, E))

task = tasks.Task(task_name)
add_task_button = ttk.Button(main_frame, text="Add Task", command=tasks.add_task(task))
add_task_button.grid(column=2, row=2, sticky=(W, E))

ttk.Label(main_frame, text=str(tasks.tasks)).grid(column=3, row=3, sticky=(W, E))

root.mainloop()
# TEST 2
