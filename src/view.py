import tkinter as tk
from tkinter import messagebox, simpledialog, font
from tkcalendar import Calendar

class TaskView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.custom_font = font.Font(family="Helvetica", size=12)
        self.main_frame = tk.Frame(root, bg="#f4f4f5")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.login_frame = tk.Frame(self.main_frame, bg="#f4f4f5")
        self.login_frame.pack(fill=tk.BOTH, expand=True)
        self.create_login_screen()

    def create_login_screen(self):
        self.login_label = tk.Label(self.login_frame, text="Bem-vindo ao Organizador de Tarefas", font=("Helvetica", 20), bg="#f4f4f5", fg="#4A4A4A")
        self.login_label.pack(pady=30)

        self.username_label = tk.Label(self.login_frame, text="Nome de Usuário:", font=self.custom_font, bg="#f4f4f5", fg="#4A4A4A")
        self.username_label.pack(pady=5)

        self.username_entry = tk.Entry(self.login_frame, font=self.custom_font)
        self.username_entry.pack(pady=5)

        self.password_label = tk.Label(self.login_frame, text="Senha:", font=self.custom_font, bg="#f4f4f5", fg="#4A4A4A")
        self.password_label.pack(pady=5)

        self.password_entry = tk.Entry(self.login_frame, font=self.custom_font, show="*")
        self.password_entry.pack(pady=5)

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.controller.login, bg="#3D9BE9", fg="white", font=self.custom_font, relief="flat", width=20)
        self.login_button.pack(pady=30)

    def show_tasks_screen(self, username):
        self.login_frame.pack_forget()

        self.navbar = tk.Frame(self.main_frame, bg="#3D9BE9", height=60)
        self.navbar.pack(fill=tk.X)

        self.navbar_label = tk.Label(self.navbar, text=f"Olá, {username}!", font=("Helvetica", 16), fg="white", bg="#3D9BE9")
        self.navbar_label.pack(side=tk.LEFT, padx=10)

        self.logout_button = tk.Button(self.navbar, text="Logout", command=self.controller.logout, bg="#f44336", fg="white", font=self.custom_font, relief="flat")
        self.logout_button.pack(side=tk.RIGHT, padx=10)

        self.sidebar = tk.Frame(self.main_frame, bg="#2E3A59", width=250)
        self.sidebar.pack(side=tk.LEFT, fill=tk.Y)
 
        self.sidebar_home_button = tk.Button(self.sidebar, text="Início", command=self.controller.show_tasks, bg="#2E3A59", fg="white", font=self.custom_font, relief="flat", width=20)
        self.sidebar_home_button.pack(pady=10)

        self.sidebar_settings_button = tk.Button(self.sidebar, text="Configurações", bg="#2E3A59", fg="white", font=self.custom_font, relief="flat", width=20)
        self.sidebar_settings_button.pack(pady=10)

        self.tasks_frame = tk.Frame(self.main_frame, bg="#f4f4f5")
        self.tasks_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=30, pady=10)

        self.backlog_frame = tk.Frame(self.main_frame)
        self.backlog_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

        self.todo_frame = tk.Frame(self.main_frame)
        self.todo_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

        self.done_frame = tk.Frame(self.main_frame)
        self.done_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

        self.progress_frame = tk.Frame(self.main_frame)
        self.progress_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

        # Backlog
        self.back_log = tk.Label(self.backlog_frame, text="Backlog", font=("Arial", 12, "bold"))
        self.back_log.pack()
        self.backlog_listbox = tk.Listbox(self.backlog_frame, width=30, height=10)
        self.backlog_listbox.pack(pady=10)
        self.btn_add = tk.Button(self.backlog_frame, text="Adicionar Tarefa", command=self.controller.add_task, bg="#4CAF50", fg="white", font=self.custom_font, relief="flat", width=15)
        self.btn_add.pack(side=tk.LEFT, padx=30, pady=10)

        # To-Do
        self.todo = tk.Label(self.todo_frame, text="To-Do", font=("Arial", 12, "bold"))
        self.todo.pack()
        self.todo_listbox = tk.Listbox(self.todo_frame, width=30, height=10)
        self.todo_listbox.pack(pady=10)
        self.btn_remove = tk.Button(self.todo_frame, text="Remover Tarefa", command=self.controller.remove_task, bg="#f44336", fg="white", font=self.custom_font, relief="flat", width=15)
        self.btn_remove.pack(side=tk.LEFT, padx=30, pady=10)

        # Progress
        self.progress = tk.Label(self.progress_frame, text='In Progress', font=("Arial", 12, "bold"))
        self.progress.pack()
        self.progress_listbox = tk.Listbox(self.progress_frame, width=30, height=10)
        self.progress_listbox.pack(pady=10)
        self.btn_clear = tk.Button(self.progress_frame, text="Limpar Tarefas", command=self.controller.clear_tasks, bg="#FF9800", fg="white", font=self.custom_font, relief="flat", width=15)
        self.btn_clear.pack(side=tk.LEFT, padx=20, pady=10)

        # Done
        self.done = tk.Label(self.done_frame, text='Done', font=("Arial", 12, "bold"))
        self.done.pack()
        self.done_listbox = tk.Listbox(self.done_frame, width=30, height=10)
        self.done_listbox.pack(pady=10)
        self.btn_edit = tk.Button(self.done_frame, text="Editar Tarefa", command=self.controller.edit_task, bg="#2196F3", fg="white", font=self.custom_font, relief="flat", width=15)
        self.btn_edit.pack(side=tk.LEFT, padx=20, pady=10)

    def update_task_list(self, tasks):
        self.tasks_frame.pack_forget()
        self.tasks_frame = tk.Frame(self.main_frame, bg="#f4f4f5")
        self.tasks_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=30, pady=10)

        self.task_listbox = tk.Listbox(self.tasks_frame, bg="#ffffff", font=self.custom_font, selectmode=tk.SINGLE)
        self.task_listbox.pack(fill=tk.BOTH, expand=True)

        for task in tasks:
            task_text = f"{task.task} - Categoria: {task.category} - Prioridade: {task.priority} - Data: {task.due_date.strftime('%d/%m/%Y') if task.due_date else 'Sem data'} - Status: {task.status}"
            self.task_listbox.insert(tk.END, task_text)

    def get_selected_task_index(self, listbox_name):
        listboxes = {
            "backlog": self.backlog_listbox,
            "todo": self.todo_listbox,
            "progress": self.progress_listbox,
            "done": self.done_listbox
        }
        
        listbox = listboxes.get(listbox_name)
        if listbox:
            selection = listbox.curselection()
            return selection[0] if selection else None
        return None
