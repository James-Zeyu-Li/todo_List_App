"""
This is a practice project to create a to do list application using python.
"""

from view.todo_GUI import TodoGUI
from controller.todo_controller import TodoController
from model.todo_model import Todo


def main():

    try:
        model = Todo()
        controller = TodoController(model, None)
        gui = TodoGUI(controller)
        controller.view = gui  # 设置视图引用
        controller.run()
    except ValueError as ex:
        print(type(ex), ex)
    except TypeError as ex:
        print(type(ex), ex)
    except IndexError as ex:
        print(type(ex), ex)


if __name__ == "__main__":
    main()
