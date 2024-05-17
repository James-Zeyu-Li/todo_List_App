"""
This is a practice project to create a to do list application using python.
"""

import sys
from PyQt5.QtWidgets import QApplication
from controller.todo_controller import TodoController
from model.todo_model import Todo
from view.todo_GUI import TodoGUI


def main():
    """
    Main function to initialize and run the todo list application.
    It sets up the MVC components and handles potential exceptions.
    """
    try:
        app = QApplication(sys.argv)
        model = Todo()
        controller = TodoController(model)
        gui = TodoGUI(controller)
        controller.view = gui
        gui.run()
        sys.exit(app.exec_())
    except ValueError as ex:
        print(f"ValueError occurred: {ex}")
    except TypeError as ex:
        print(f"TypeError occurred: {ex}")
    except IndexError as ex:
        print(f"IndexError occurred: {ex}")


if __name__ == "__main__":
    main()
