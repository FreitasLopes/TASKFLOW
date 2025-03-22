from abc import ABC, abstractmethod
from model import Task

class TaskFactory(ABC):
    @abstractmethod
    def create_task(self, task_name, priority, category, due_date):
        pass

class LowPriorityTaskFactory(TaskFactory):
    def create_task(self, task_name, priority, category, due_date):
        return Task(task_name, "Baixa", category, due_date)

class MediumPriorityTaskFactory(TaskFactory):
    def create_task(self, task_name, priority, category, due_date):
        return Task(task_name, "Média", category, due_date)

class HighPriorityTaskFactory(TaskFactory):
    def create_task(self, task_name, priority, category, due_date):
        return Task(task_name, "Alta", category, due_date)
