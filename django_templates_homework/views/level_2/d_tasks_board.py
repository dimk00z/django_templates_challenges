"""
Оживите шаблон.
"""

from dataclasses import dataclass
from enum import StrEnum

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


class TaskStatus(StrEnum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


@dataclass
class Task:
    title: str
    status: TaskStatus


def get_tasks_by_status(
    tasks: list[Task],
    status: TaskStatus,
) -> tuple[Task, ...]:
    return tuple(task for task in tasks if task.status == status)


def tasks_board_view(request: HttpRequest) -> HttpResponse:
    tasks: list[Task] = [
        Task(title="Помыть посуду", status=TaskStatus.IN_PROGRESS),
        Task(title="Вымыть пол", status=TaskStatus.TODO),
        Task(title="Выспаться", status=TaskStatus.DONE),
        Task(title="Посмотреть кино", status=TaskStatus.DONE),
        Task(title="Застелить кровать", status=TaskStatus.IN_PROGRESS),
        Task(title="Купить продуктов", status=TaskStatus.DONE),
    ]
    return render(
        request,
        "level_2/tasks_board.html",
        context={
            "tasks_in_progress": get_tasks_by_status(
                tasks,
                TaskStatus.IN_PROGRESS,
            ),
            "tasks_done": get_tasks_by_status(
                tasks,
                TaskStatus.DONE,
            ),
            "tasks_todo": get_tasks_by_status(
                tasks,
                TaskStatus.TODO,
            ),
        },
    )
