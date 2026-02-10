"""
Adds class and methods for handling tasks.
"""

import datetime as dt
import typing

_priority = typing.Literal["low", "normal", "high"]


class Task(typing.TypedDict):
    """
    A dictionary representing a task.
    Keys and values in order:
        name: str, containing the name of the task e.g. "Write chapter 3"
        priority: str, containing one of "low", "normal", "high" defaulting to normal
        deadline: datetime.datetime, othewise no deadline
        description: str, containing a more detailed explanation of the task
    """

    name: str
    priority: _priority
    deadline: dt.datetime | None
    description: str | None


tasks: typing.List[Task] = []  # Holds all the tasks


def clear_tasks() -> None:
    """
    Removes all tasks.
    """
    tasks.clear()


def create_task(
    name: str,
    priority: _priority = "normal",
    deadline: dt.datetime | None = None,
    description: str | None = None,
) -> Task:
    return Task(
        name=name, priority=priority, deadline=deadline, description=description
    )


def add_task(task: Task) -> None:
    """
    Adds a task.
    """
    tasks.append(task)


def remove_task(input_task: Task) -> Task:
    """
    Removes input_task.
    Returns the removed task.
    Raises ValueError if input_task not in tasks.
    """
    for i, task in enumerate(tasks):
        if task is input_task:
            return tasks.pop(i)

    raise ValueError("input_task argument must contain a task in tasks")


def remove_task_name(input_name: str) -> Task:
    """
    Removes input_task based on its name.
    If multiple tasks have the same name, removes the first.
    Returns the removed task.
    Raises ValueError if input_task not in tasks.
    """
    for i, task in enumerate(tasks):
        if task["name"] == input_name:
            return tasks.pop(i)

    raise ValueError("input_name argument must contain a task in tasks")


def get_tasks_count() -> int:
    """
    Returns number of tasks.
    """
    return len(tasks)


def show_task(input_task: Task) -> str:
    """
    Nicely displaces the task info to an end user, not including deadline.
    input_task: Task
    Returns str with nice formatting of values
    Raises ValueError if input_task not in tasks.
    """
    return f"Name: {input_task['name']}, Priority: {input_task['priority']}"

    raise ValueError("input_task argument must contain a task in tasks")


def show_task_name(input_name: str) -> str:
    """
    Nicely displaces the task info to an end user, not including deadline.
    input_name: str takes name of task
    If multiple tasks have the same name, shows the first.
    Returns str with nice formatting of values
    Raises ValueError if input_task not in tasks.
    """
    for i, task in enumerate(tasks):
        if task["name"] == input_name:
            return f"Name: {task['name']}, Priority: {task['priority']}"

    raise ValueError("input_name argument must contain a task in tasks")
