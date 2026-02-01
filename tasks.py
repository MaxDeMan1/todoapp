"""
Adds class and methods for handling tasks.
"""

import datetime as dt
import typing

_priority = typing.Literal["low", "normal", "high"]


class task:
    """
    Parameters:
        name = str containing the name of the task e.g. "Write chapter 3"
        priority = str containing one of "low", "normal", "high" defaulting to normal
        deadline = datetime.datetime, othewise no deadline
        description = str containing a more detailed explanation of the task
    """

    def __init__(
        self,
        name: str,
        priority: _priority = "normal",
        deadline: dt.datetime | None = None,
        description: str | None = None,
    ):
        self.name: str = name
        self.priority: _priority = priority
        self.deadline: dt.datetime | None = deadline
        self.description = description

    def __repr__(self):
        return f"task(name = {self.name}, priority = {self.priority}, deadline = {self.deadline})"
