from abc import ABC, abstractmethod
from managers.abstracts import AbstractPrintingManager, AbstractTodoManager


class Manager(ABC):
    @abstractmethod
    def toDoManager(self) -> AbstractTodoManager.TodoManager:
        pass

    @abstractmethod
    def printingManager(self) -> AbstractPrintingManager.PritingManager:
        pass
