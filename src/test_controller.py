import pytest
from unittest.mock import MagicMock, patch
from controller import TaskController
from model import TaskModel
from view import TaskView

@pytest.fixture
def controller():
    root = MagicMock()
    controller = TaskController(root)
    controller.view = MagicMock(spec=TaskView)
    controller.model = MagicMock(spec=TaskModel)
    return controller

def test_login_with_username(controller):
    controller.view.username_entry.get.return_value = "usuario_teste"
    controller.login()
    controller.view.show_tasks_screen.assert_called_once_with("usuario_teste")

def test_login_without_username(controller):
    controller.view.username_entry.get.return_value = ""
    with patch("tkinter.messagebox.showerror") as mock_showerror:
        controller.login()
        mock_showerror.assert_called_once_with("Erro", "Nome de usuário inválido.")

def test_logout(controller):
    with patch("tkinter.messagebox.askyesno", return_value=True):
        controller.logout()
        controller.view.root.destroy.assert_called_once()

def test_show_tasks(controller):
    controller.model.tasks = ["task1", "task2"]
    controller.show_tasks()
    controller.view.update_task_list.assert_called_once_with(["task1", "task2"])

def test_clear_tasks(controller):
    with patch("tkinter.messagebox.askyesno", return_value=True):
        controller.clear_tasks()
        controller.model.clear_tasks.assert_called_once()
        for listbox in [
            controller.view.backlog_listbox,
            controller.view.todo_listbox,
            controller.view.progress_listbox,
            controller.view.done_listbox
        ]:
            listbox.delete.assert_called()

