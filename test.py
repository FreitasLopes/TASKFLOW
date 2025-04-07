import tkinter as tk

class KanbanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kanban Board")

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Criando os Frames das colunas
        self.backlog_frame = tk.Frame(self.main_frame)
        self.backlog_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

        self.todo_frame = tk.Frame(self.main_frame)
        self.todo_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

        self.concluido_frame = tk.Frame(self.main_frame)
        self.concluido_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

        # Backlog Column
        self.back_log = tk.Label(self.backlog_frame, text="Backlog", font=("Arial", 12, "bold"))
        self.back_log.pack()

        self.backlog_listbox = tk.Listbox(self.backlog_frame, width=30, height=10)
        self.backlog_listbox.pack(pady=10)

        self.btn_add = tk.Button(self.backlog_frame, text="Adicionar Tarefa", bg="#4CAF50", fg="white", relief="flat", width=15)
        self.btn_add.pack(pady=10)

        # To-Do Column
        self.todo = tk.Label(self.todo_frame, text="To-Do", font=("Arial", 12, "bold"))
        self.todo.pack()

        self.todo_listbox = tk.Listbox(self.todo_frame, width=30, height=10)
        self.todo_listbox.pack(pady=10)

        self.btn_edit = tk.Button(self.todo_frame, text="Editar Tarefa", bg="#2196F3", fg="white", relief="flat", width=15)
        self.btn_edit.pack(pady=10)

        # Concluído Column
        self.concluido = tk.Label(self.concluido_frame, text="Concluído", font=("Arial", 12, "bold"))
        self.concluido.pack()

        self.concluido_listbox = tk.Listbox(self.concluido_frame, width=30, height=10)
        self.concluido_listbox.pack(pady=10)

        self.btn_remove = tk.Button(self.concluido_frame, text="Remover Tarefa", bg="#f44336", fg="white", relief="flat", width=15)
        self.btn_remove.pack(pady=10)

        self.btn_clear = tk.Button(self.concluido_frame, text="Limpar Tarefas", bg="#FF9800", fg="white", relief="flat", width=15)
        self.btn_clear.pack(pady=10)

# Criando a janela principal
root = tk.Tk()
app = KanbanApp(root)
root.mainloop()
