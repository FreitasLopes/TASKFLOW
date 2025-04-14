from datetime import datetime
from database import create_table, add_task, remove_task, update_task, get_all_tasks, clear_all_tasks

class Task:
    def __init__(self, id, task, priority, category, due_date):
        self.id = id
        self.task = task
        self.priority = priority
        self.category = category
        self.due_date = due_date

class TaskModel:
    def __init__(self):
        create_table()
        self.tasks = self.load_tasks()

    def load_tasks(self):
        task_data = get_all_tasks()
        return [
            Task(
                data["id"],
                data["task"],
                data["priority"],
                data["category"],
                data["due_date"]
            ) for data in task_data
        ]

    def add_task(self, task):
        add_task(task.task, task.priority, task.category, task.due_date)
        self.tasks = self.load_tasks()

    def remove_task(self, index):
        task = self.tasks[index]
        remove_task(task.id)
        self.tasks.pop(index)

    def update_task(self, index, updated_task):
        task = self.tasks[index]
        update_task(
            task.id,
            updated_task.task,
            updated_task.priority,
            updated_task.category,
            updated_task.due_date
        )
        self.tasks[index] = updated_task

    def clear_tasks(self):
        clear_all_tasks()
        self.tasks.clear()
