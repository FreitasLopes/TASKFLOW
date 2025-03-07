
from view import TaskView
import tkinter as tk
from model import Task, TaskModel
from tkinter import simpledialog, messagebox
from datetime import datetime
from tkcalendar import Calendar
from controller import TaskController



if __name__ == "__main__":
    root = tk.Tk()
    app = TaskController(root)
    root.mainloop()