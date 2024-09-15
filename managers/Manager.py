from managers.TodoManagement import TodoManagement
from managers.PrintingMananger import PrintingMananger


class Manager:
    def __init__(self):
        self._todoManager = TodoManagement([], self)
        self._printingManager = PrintingMananger(self)

    @property
    def todoManager(self) -> TodoManagement:
        return self._todoManager

    @property
    def printingManager(self) -> PrintingMananger:
        return self._printingManager
