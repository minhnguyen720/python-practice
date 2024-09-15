from abc import ABC, abstractmethod
from entities.ToDo import Todo


class PritingManager(ABC):
    @abstractmethod
    def showGeneralInstructions(self):
        pass

    @abstractmethod
    def showGreeting(self, param):
        pass

    @abstractmethod
    def showUserCmd(self, currentState: str):
        pass

    @abstractmethod
    def showTodo(todo: Todo):
        pass
