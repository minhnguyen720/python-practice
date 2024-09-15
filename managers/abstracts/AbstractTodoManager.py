from abc import ABC, abstractmethod
from entities.ToDo.Todo import Todo
from typing import List


class TodoManager(ABC):
    @abstractmethod
    def addItem(self):
        pass

    @abstractmethod
    def updateItem(self, itemId: str):
        pass

    @abstractmethod
    def removeItem(self, itemId: str):
        pass

    @abstractmethod
    def getToDoList(self) -> List[Todo]:
        pass

    @abstractmethod
    def setTodoList(self, newList: List[Todo]):
        pass
