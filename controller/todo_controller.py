"""
This is a practice project to create a to do list application using python.
"""


class TodoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_view(self):
        self.show_item()

    def add_item(self):
        item = self.view.get_item_text()
        self.model.add_item(item)
        self.view.clear_item_text()

    def show_item(self):
        items = self.model.current_item()
        self.view.show_items(items)

    def edit_item(self):
        index = self.view.get_index()
        new_item = self.view.get_new_item()
        self.model.edit_item(index, new_item)

    def mark_complete(self):
        index = self.view.get_index()
        self.model.mark_complete(index)

    def run(self):
        self.view.set_controller(self)
        self.view.run()
