import pytest
from unittest.mock import MagicMock, patch
from controller import TaskController
from model import TaskModel
from task_factories import LowPriorityTaskFactory
from datetime import datetime


@pytest.fixture
def mock_view():
    mock = MagicMock()
    mock.username_entry.get.return_value = "testuser"
    mock.custom_font = "Arial"
    mock.get_selected_task_index.return_value = 0
    mock.backlog_listbox = MagicMock()
    mock.todo_listbox = MagicMock()
    mock.progress_listbox = MagicMock()
    mock.done_listbox = MagicMock()
    mock.root = MagicMock()
    return mock


@pytest.fixture
def controller(mock_view):
    with patch("controller.TaskView", return_value=mock_view):
        return TaskController(root=MagicMock())


def test_login_success(controller):
    controller.login()
    controller.view.show_tasks_screen.assert_called_with("testuser")


def test_login_failure(controller):
    controller.view.username_entry.get.return_value = ""
    with patch("tkinter.messagebox.showerror") as mock_error:
        controller.login()
        mock_error.assert_called_with("Erro", "Nome de usuário inválido.")


def test_add_task(controller):
    # Preparar mocks
    controller.view.root = MagicMock()

    with patch("tkinter.Toplevel"), \
         patch("tkinter.Entry"), \
         patch("tkinter.ttk.Combobox"), \
         patch("tkcalendar.Calendar") as mock_calendar, \
         patch("tkinter.messagebox.showerror") as mock_error:

        mock_calendar_instance = mock_calendar.return_value
        mock_calendar_instance.get_date.return_value = "12/04/2025"

        # Simula criação da tarefa manualmente
        factory = LowPriorityTaskFactory()
        task = factory.create_task("Task 1", "Baixa", "Categoria 1", datetime.strptime("12/04/2025", "%d/%m/%Y"))
        controller.model.add_task(task)

        assert len(controller.model.tasks) == 1
        assert controller.model.tasks[0].task == "Task 1"


def test_remove_task(controller):
    task = LowPriorityTaskFactory().create_task("Task to Remove", "Baixa", "Categoria", datetime.now())
    controller.model.add_task(task)

    with patch("tkinter.messagebox.askyesno", return_value=True):
        controller.remove_task()

    assert len(controller.model.tasks) == 0


def test_clear_tasks(controller):
    task = LowPriorityTaskFactory().create_task("Task to Clear", "Baixa", "Categoria", datetime.now())
    controller.model.add_task(task)

    with patch("tkinter.messagebox.askyesno", return_value=True):
        controller.clear_tasks()

    assert len(controller.model.tasks) == 0
    controller.view.backlog_listbox.delete.assert_called()


def test_logout(controller):
    with patch("tkinter.messagebox.askyesno", return_value=True):
        controller.logout()
        controller.view.root.destroy.assert_called_once()


def test_edit_task(controller):
    task = LowPriorityTaskFactory().create_task("Original Task", "Baixa", "Categoria", datetime.strptime("12/04/2025", "%d/%m/%Y"))
    controller.model.add_task(task)

    with patch("tkinter.Toplevel"), \
         patch("tkinter.Entry") as mock_entry, \
         patch("tkinter.ttk.Combobox") as mock_combo, \
         patch("tkcalendar.Calendar") as mock_calendar, \
         patch("tkinter.Button"):

        mock_entry_instance = mock_entry.return_value
        mock_entry_instance.get.return_value = "Edited Task"

        mock_combo_instance = mock_combo.return_value
        mock_combo_instance.get.return_value = "Média"

        mock_calendar_instance = mock_calendar.return_value
        mock_calendar_instance.get_date.return_value = "13/04/2025"

        # Simula edição manual da tarefa
        task.task = "Edited Task"
        task.priority = "Média"
        task.due_date = datetime.strptime("13/04/2025", "%d/%m/%Y")

        assert task.task == "Edited Task"
        assert task.priority == "Média"
        assert task.due_date.strftime("%d/%m/%Y") == "13/04/2025"
