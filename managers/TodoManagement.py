from entities.ToDo.Todo import Todo
import utils.utils as utils
import uuid
import datetime
from typing import List
from managers.PrintingMananger import AppState
from managers.abstracts.AbstractManager import Manager
from managers.abstracts.AbstractTodoManager import TodoManager


class TodoManagement(TodoManager):
    def __init__(self, list: List[Todo], manager: Manager) -> None:
        self._todoList = list
        self._manager = manager

    def addItem(self):
        self._showInstrctions()
        userCmd = ""
        title = ""
        content = ""
        while userCmd != "q":
            printManager = self._manager.printingManager
            userCmd = printManager.showUserCmd(
                AppState.CREATE.value, utils.DEFAULT_COMMAND
            )
            match userCmd:
                case "1":
                    title = input("Enter todo title: ")
                case "2":
                    content = input("Enter todo content: ")
                case "3":
                    print("CURRENT INPUT")
                    print(f"Title: {title}")
                    print(f"Content: {content}")
                case "4":
                    print("NOTICE: Added")
                    newTodo = Todo(uuid.uuid4(), title, content, datetime.date.today())
                    self._todoList.append(newTodo)
                    for todo in self._todoList:
                        print(utils.DIVIDER)
                        print(f"ID: {todo.id}")
                        print(f"Title: {todo.title}")
                        print(f"Content: {todo.content}")
                        print(f"Created date: {todo.createdDate}")
                        print(utils.DIVIDER + "\n")
                    userCmd = "q"
                case "help":
                    self._showInstrctions()
                case "q":
                    print("Back to MAIN")
                case _:
                    print("Invalid command")

    def updateItem(self, itemId):
        print("updated")

    def removeItem(self, itemId: str):
        isExisted = False
        for i in range(len(self._todoList)):
            if str(self._todoList[i].id).strip() == itemId.strip():
                del self._todoList[i]
                isExisted = True
                break
        if isExisted:
            print("Removed")
        else:
            print("Item not found")

    def getToDoList(self):
        return self._todoList

    def setTodoList(self, newList):
        self._todoList = newList

    def _showInstrctions(self):
        print("CREATE NEW TODO ITEM: ")
        print("[1] Add title")
        print("[2] Add content")
        print("[3] Current input")
        print("[4] Create")
        print("[help] Show available commands")
        print("[q] Cancel\n")
