from abc import ABC, abstractmethod
from datetime import datetime


class Todo(ABC):
    @abstractmethod
    def id(self) -> str:
        """Returns the unique ID of the todo."""
        pass

    @abstractmethod
    def title(self) -> str:
        """Returns the title of the todo."""
        pass

    @abstractmethod
    def content(self) -> str:
        """Returns the content of the todo."""
        pass

    @abstractmethod
    def createdDate(self) -> datetime:
        """Returns the creation date of the todo."""
        pass
