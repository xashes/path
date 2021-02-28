#!/usr/bin/env python3

from enum import Enum
import reprlib


class Todo:
    def __init__(self, content: str, status: str = None):
        self.content = content
        self.status = status

    def __repr__(self) -> str:
        return f"Todo({reprlib.repr(self.content)})"


class TodoStatus(str, Enum):
    next = "Next"


class TodoList:
    def __init__(self, title: str) -> None:
        self.title = title
        self.items = []

    def __iter__(self):
        for item in self.items:
            yield item
        return

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return f"TodoList({reprlib.repr(self.title)})"

    def add_todo(self, content: str):
        todo = Todo(content)
        self.items.append(todo)


if __name__ == "__main__":
    tl = TodoList("title")
    print(tl.__dict__)
