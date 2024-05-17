"""
This is a practice project to create a to do list application using python.
"""
from typing import Optional
from model.todo_model import Todo
from view.todo_GUI import TodoGUI


class TodoController:
    def __init__(self, model: Todo, view: Optional[TodoGUI] = None):
        self.model = model
        self.view = view

    def update_view(self):
        """
        Update the view to display the current items in the todo list.
        """
        items = self.model.current_item()
        if self.view is not None:
            self.view.show_items(items)
        else:
            raise ValueError("View is not set in the controller.")

    def add_item(self, item=None):
        """
        Add a new item to the todo list.

        Args:
            item (str): The item to add.
        """
        if item is None:
            if self.view is not None:
                item = self.view.get_item_text()
            else:
                raise ValueError("View is not set in the controller.")

        if item.strip():
            self.model.add_item(item)
            if self.view is not None:
                self.view.clear_item_text()
                self.update_view()
        else:
            if self.view is not None:
                self.view.show_error("Item cannot be empty.")
            else:
                raise ValueError("View not set in controller")

    def show_items(self):
        """
        Show all current items in the todo list.
        """
        items = self.model.current_item()
        if items is not None:
            return items
        else:
            return []

    def edit_item(self, index, new_item):
        """
        Edit an existing item in the todo list.

        Args:
            index (int): The index of the item to edit.
            new_item (str): The item to edit.
        """
        if self.model.edit_item(index, new_item):
            self.update_view()
        else:
            if self.view is not None:
                self.view.show_error("Index out of range")

    def mark_complete(self, index):
        """
        Mark an item in the todo list as complete.

        Args:
            index (int): The index of the item to mark complete.
        """
        self.model.mark_complete(index)
        self.update_view()

    def run(self):
        """
        run the application
        """
        if self.view is not None:
            self.view.run()
        else:
            raise ValueError("View is not set in the controller.")
