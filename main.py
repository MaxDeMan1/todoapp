from tkinter import *
from tkinter import ttk

root = Tk()
root.title("todoapp")
main_frame = ttk.Frame(root, padding=(3, 3, 12, 12))
main_frame.grid(column=0, row=0, sticky=(N, W, E, S))

root.mainloop()
