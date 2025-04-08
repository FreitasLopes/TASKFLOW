from model import TaskModel  
from task_factories import LowPriorityTaskFactory, MediumPriorityTaskFactory, HighPriorityTaskFactory
from view import TaskView
import tkinter as tk
from tkinter import simpledialog, messagebox 
from datetime import datetime
from tkcalendar import Calendar

class TaskController:
    def __init__(self, root):
        self.model = TaskModel()  
        self.view = TaskView(root, self) 

    def login(self):
        username = self.view.username_entry.get()
        password = self.view.password_entry.get()

        if username and password:
            self.view.show_tasks_screen(username)
        else:
            messagebox.showerror("Erro", "Nome de usuário ou senha inválidos.")

    def show_tasks(self):
            self.view.update_task_list(self.model.tasks)

    def logout(self):
        self.view.main_frame.pack_forget()

    def add_task(self):
        task_window = tk.Toplevel(self.view.root)
        task_window.title("Adicionar Tarefa")

        task_label = tk.Label(task_window, text="Tarefa:", font=self.view.custom_font)
        task_label.pack(pady=5)
        task_entry = tk.Entry(task_window, font=self.view.custom_font)
        task_entry.pack(pady=5)

        priority_label = tk.Label(task_window, text="Prioridade (Baixa, Média, Alta):", font=self.view.custom_font)
        priority_label.pack(pady=5)
        priority_entry = tk.Entry(task_window, font=self.view.custom_font)
        priority_entry.pack(pady=5)

        category_label = tk.Label(task_window, text="Categoria:", font=self.view.custom_font)
        category_label.pack(pady=5)
        category_entry = tk.Entry(task_window, font=self.view.custom_font)
        category_entry.pack(pady=5)

        calendar_label = tk.Label(task_window, text="Data de Vencimento:", font=self.view.custom_font)
        calendar_label.pack(pady=5)
        cal = Calendar(task_window, selectmode="day", date_pattern="dd/mm/yyyy")
        cal.pack(pady=10)

        def save_task():
            task = task_entry.get()
            priority = priority_entry.get()
            category = category_entry.get()
            date = cal.get_date()
            due_date = datetime.strptime(date, "%d/%m/%Y") if date else None

            if task and priority and category:
                # Aqui, criamos a fábrica baseada na prioridade
                if priority.lower() == "baixa":
                    factory = LowPriorityTaskFactory()
                elif priority.lower() == "média":
                    factory = MediumPriorityTaskFactory()
                elif priority.lower() == "alta":
                    factory = HighPriorityTaskFactory()
                else:
                    messagebox.showerror("Erro", "Prioridade inválida!")
                    return

                new_task = factory.create_task(task, priority, category, due_date)
                self.model.add_task(new_task)
                self.view.update_task_list(self.model.tasks)
                task_window.destroy()

        save_button = tk.Button(task_window, text="Salvar Tarefa", command=save_task, bg="#4CAF50", fg="white", font=self.view.custom_font)
        save_button.pack(pady=10)
        
    def remove_task(self):
            index = self.view.get_selected_task_index()
            if index is not None:
                self.model.remove_task(index)
                self.view.update_task_list(self.model.tasks)

    def clear_tasks(self):
        if messagebox.askyesno("Confirmação", "Deseja limpar todas as tarefas?"):
            self.model.clear_tasks()
            self.view.update_task_list(self.model.tasks)

    def edit_task(self):
        index = self.view.get_selected_task_index()
        if index is not None:
            task = self.model.tasks[index]
            new_task = simpledialog.askstring("Editar Tarefa", "Alterar a tarefa:", initialvalue=task.task)
            if new_task:
                task.task = new_task
                self.view.update_task_list(self.model.tasks)
