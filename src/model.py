import datetime

class Task:
    def __init__(self, task, priority, category, due_date):
        self.task = task
        self.priority = priority
        self.category = category
        self.due_date = due_date
        self.status = "Pendente"
        self.created_at = datetime.datetime.now()
        self.color = self.get_color_by_priority()

    def get_color_by_priority(self):
        if self.priority.lower() == "alta":
            return "#FF5722"
        elif self.priority.lower() == "mÃ©dia":
            return "#FFEB3B"
        elif self.priority.lower() == "baixa":
            return "#8BC34A"
        return "#ffffff"

class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def clear_tasks(self):
        self.tasks.clear()

    def edit_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index].task = new_task

