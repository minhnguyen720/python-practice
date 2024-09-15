from utils.utils import GREETING_ART, DIVIDER, GOOD_BYE_ART, BOOK_ART
from enum import Enum
from entities.ToDo.AbstractTodo import Todo
from managers.abstracts.AbstractManager import Manager


class AppState(Enum):
    MAIN = "main"
    CREATE = "create"


class GreetingType(Enum):
    START = "start"
    END = "end"


class PrintingMananger:
    def __init__(self, manager: Manager) -> None:
        self._manager = manager

    def showGeneralInstructions(self):
        """Shows the available commands."""
        print("Available commands:")
        print("[1] show_todos: Show all to-do items")
        print("[2] add_todo: Add a new to-do item")
        print("[3] remove_todo: Remove an existing to-do item")
        print("[help] show_instructions: Show these instructions")
        print("[q] Quit\n")

    def showGreeting(self, param: GreetingType):
        print(DIVIDER)
        if param == GreetingType.START:
            print(GREETING_ART)
        elif param == GreetingType.END:
            print(GOOD_BYE_ART)
        else:
            print(BOOK_ART)
        print(DIVIDER)

    def showUserCmd(self, currentState: str, message: str):
        return input(f"[{currentState.upper()}] {message} ")

    def showTodo(self, todo: Todo):
        print(DIVIDER)
        print(f"ID: {todo.id}")
        print(f"Title: {todo.title}")
        print(f"Content: {todo.content}")
        print(f"Created date: {todo.createdDate}")
        print(DIVIDER + "\n")
