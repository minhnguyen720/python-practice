from managers.Manager import Manager
from managers.PrintingMananger import AppState
from managers.PrintingMananger import GreetingType
import utils.utils as utils


class App:
    def __init__(self):
        self._manager = Manager()

    def start(self):
        userCmd = ""
        printManager = self._manager.printingManager

        printManager.showGreeting(GreetingType.START)
        printManager.showGeneralInstructions()
        while userCmd != "q":
            userCmd = printManager.showUserCmd(
                AppState.MAIN.value, utils.DEFAULT_COMMAND
            )
            match userCmd:
                case "1":
                    todoList = self._manager.todoManager.getToDoList()
                    for todo in todoList:
                        printManager.showTodo(todo)
                case "2":
                    self._manager.todoManager.addItem()
                case "3":
                    userCmd = printManager.showUserCmd(
                        AppState.MAIN,
                        "Input the Todo item's ID that you want to delete:\n",
                    )
                    self._manager.todoManager.removeItem(userCmd)
                case "help":
                    printManager.showGeneralInstructions()
                case "q":
                    print("Closing...")
                case _:
                    print("Invalid command")
                    print(
                        "Check the instruction again by typing 'help' to your command line\n"
                    )

        printManager.showGreeting(GreetingType.END)
