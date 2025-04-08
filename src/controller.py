from model import TaskModel  
from task_factories import LowPriorityTaskFactory, MediumPriorityTaskFactory, HighPriorityTaskFactory
from view import TaskView
import tkinter as tk
from tkinter import messagebox, ttk
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
        confirm = messagebox.askyesno("Confirmação", "Tem certeza que deseja sair?")
        if confirm:
            self.view.root.destroy()

    def add_task(self):
        task_window = tk.Toplevel(self.view.root)
        task_window.title("Adicionar Tarefa")

        tk.Label(task_window, text="Tarefa:", font=self.view.custom_font).pack(pady=5)
        task_entry = tk.Entry(task_window, font=self.view.custom_font)
        task_entry.pack(pady=5)

        tk.Label(task_window, text="Prioridade:", font=self.view.custom_font).pack(pady=5)
        priority_combo = ttk.Combobox(task_window, font=self.view.custom_font, state="readonly", values=("Baixa", "Média", "Alta"))
        priority_combo.pack(pady=5)
        priority_combo.current(0)

        tk.Label(task_window, text="Categoria:", font=self.view.custom_font).pack(pady=5)
        category_entry = tk.Entry(task_window, font=self.view.custom_font)
        category_entry.pack(pady=5)

        tk.Label(task_window, text="Data de Vencimento:", font=self.view.custom_font).pack(pady=5)
        cal = Calendar(task_window, selectmode="day", date_pattern="dd/mm/yyyy")
        cal.pack(pady=10)

        def save_task():
            task = task_entry.get().strip()
            priority = priority_combo.get().strip()
            category = category_entry.get().strip()
            date = cal.get_date()
            due_date = datetime.strptime(date, "%d/%m/%Y") if date else None

            if task and priority and category:
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

                self.view.backlog_listbox.insert(tk.END, f"{task} - {priority} - {category} - {due_date.strftime('%d/%m/%Y') if due_date else 'Sem data'}")
                task_window.destroy()
            else:
                messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")

        tk.Button(task_window, text="Salvar Tarefa", command=save_task, bg="#4CAF50", fg="white", font=self.view.custom_font).pack(pady=10)

    def remove_task(self):
        listboxes = {
            "backlog": self.view.backlog_listbox,
            "todo": self.view.todo_listbox,
            "progress": self.view.progress_listbox,
            "done": self.view.done_listbox
        }

        for listbox_name, listbox in listboxes.items():
            index = self.view.get_selected_task_index(listbox_name)
            if index is not None:
                task = self.model.tasks[index]
                confirm = messagebox.askyesno("Confirmar", f"Você tem certeza que deseja remover a tarefa: {task.task}?")
                if confirm:
                    self.model.remove_task(index)
                    listbox.delete(index)
                break

    def clear_tasks(self):
        if messagebox.askyesno("Confirmação", "Deseja limpar todas as tarefas?"):
            self.model.clear_tasks()

            listboxes = [
                self.view.backlog_listbox,
                self.view.todo_listbox,
                self.view.progress_listbox,
                self.view.done_listbox
            ]

            for listbox in listboxes:
                listbox.delete(0, tk.END)

    def edit_task(self):
        listboxes = {
            "backlog": self.view.backlog_listbox,
            "todo": self.view.todo_listbox,
            "progress": self.view.progress_listbox,
            "done": self.view.done_listbox
        }

        for listbox_name, listbox in listboxes.items():
            index = self.view.get_selected_task_index(listbox_name)
            if index is not None:
                task = self.model.tasks[index]

                edit_window = tk.Toplevel(self.view.root)
                edit_window.title("Editar Tarefa")

                tk.Label(edit_window, text="Editar Tarefa:", font=self.view.custom_font).pack(pady=5)
                task_entry = tk.Entry(edit_window, font=self.view.custom_font)
                task_entry.insert(0, task.task)
                task_entry.pack(pady=5)

                tk.Label(edit_window, text="Prioridade:", font=self.view.custom_font).pack(pady=5)
                priority_combo = ttk.Combobox(edit_window, font=self.view.custom_font, state="readonly", values=("Baixa", "Média", "Alta"))
                priority_combo.pack(pady=5)
                priority_combo.set(task.priority)

                tk.Label(edit_window, text="Categoria:", font=self.view.custom_font).pack(pady=5)
                category_entry = tk.Entry(edit_window, font=self.view.custom_font)
                category_entry.insert(0, task.category)
                category_entry.pack(pady=5)

                tk.Label(edit_window, text="Data de Vencimento:", font=self.view.custom_font).pack(pady=5)
                cal = Calendar(edit_window, selectmode="day", date_pattern="dd/mm/yyyy")
                if task.due_date:
                    cal.selection_set(task.due_date)
                cal.pack(pady=10)

                def save_changes():
                    new_task_name = task_entry.get().strip()
                    new_priority = priority_combo.get().strip()
                    new_category = category_entry.get().strip()
                    new_date_str = cal.get_date()

                    if not new_task_name or not new_priority or not new_category:
                        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
                        return

                    task.task = new_task_name
                    task.priority = new_priority
                    task.category = new_category
                    task.due_date = datetime.strptime(new_date_str, "%d/%m/%Y") if new_date_str else None

                    listbox.delete(index)
                    listbox.insert(
                        index,
                        f"{task.task} - {task.priority} - {task.category} - {task.due_date.strftime('%d/%m/%Y') if task.due_date else 'Sem data'}"
                    )

                    edit_window.destroy()

                tk.Button(edit_window, text="Salvar Alterações", command=save_changes, bg="#4CAF50", fg="white", font=self.view.custom_font).pack(pady=20)
                break
