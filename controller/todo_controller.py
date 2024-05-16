"""
This is a practice project to create a to do list application using python.
"""


class TodoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_view(self):
        """
        Update the view to display the current items in the todo list.
        """
        items = self.model.current_item()
        self.view.show_items(items)

    def add_item(self, item=None):
        """
        Add a new item to the todo list.

        Args:
            item (str): The item to add.
        """
        if item is None:
            item = self.view.get_item_text()
        if item.strip():
            self.model.add_item(item)
            self.view.clear_item_text()
            self.update_view()
        else:
            self.view.show_error("Item cannot be empty.")

    def show_item(self):
        """
        Show all current items in the todo list.
        """
        items = self.model.current_item()
        if items is not None:
            self.view.show_items(items)
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
            self.view.display_error("Index out of range")

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
        self.view.run()
