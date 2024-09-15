import datetime
from entities.ToDo import AbstractTodo


class Todo(AbstractTodo.Todo):
    def __init__(
        self, id: str, title: str, content: str, createdDate: datetime
    ) -> None:
        self._id = id
        self._title = title
        self._content = content
        self._createdDate = createdDate

    @property
    def id(self) -> str:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @property
    def content(self) -> str:
        return self._content

    @property
    def createdDate(self) -> datetime:
        return self._createdDate
