from PyQt5.QtWidgets import (QWidget, QVBoxLayout,
                             QLabel, QPushButton, QLineEdit, QHBoxLayout,
                             QListWidget, QInputDialog, QMessageBox)


class TodoGUI(QWidget):
    """
    View class to handle the graphical user interface of
    the todo list application using PyQt5.
    """

    def __init__(self, controller):
        super().__init__()  # make sure qwidget initiation
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        """
        Initialize the user interface.
        """
        self.setWindowTitle("Todo List APP")
        self.resize(300, 500)

        # Main layout
        self.main_layout = QVBoxLayout()

        # Label
        self.label = QLabel("Welcome to the To Do List Application")
        self.main_layout.addWidget(self.label)

        self.input_layout = QHBoxLayout()

        # Input box
        self.input_box = QLineEdit(self)
        self.input_box.setPlaceholderText("Enter your todo item here:")
        self.input_layout.addWidget(self.input_box)

        # Add button
        self.add_button = QPushButton("Add", self)
        self.add_button.clicked.connect(self.add_item)
        self.input_layout.addWidget(self.add_button)

        self.main_layout.addLayout(self.input_layout)

        # List box
        self.listbox = QListWidget(self)
        self.main_layout.addWidget(self.listbox)

        # Edit button
        self.edit_button = QPushButton("Edit", self)
        self.edit_button.clicked.connect(self.edit_item)
        self.main_layout.addWidget(self.edit_button)

        self.setLayout(self.main_layout)

    def add_item(self):
        """
        Add a new item to the todo list.
        """
        item = self.input_box.text()
        if item.strip():
            self.controller.add_item(item)
            self.clear_item_text()
            self.refresh_items()
        else:
            self.show_error("Item cannot be empty.")

    def edit_item(self):
        """
        Edit an existing item in the todo list.
        """
        selected_item = self.listbox.currentRow()
        if selected_item != -1:
            current_text = self.controller.model.current_item()[
                selected_item].strip()
            new_item, ok = QInputDialog.getText(
                self, "Edit Item", "Enter new item text:", text=current_text)
            if ok and new_item:
                self.controller.edit_item(selected_item, new_item)
                self.refresh_items()
        else:
            self.show_error("No item selected.")



    def show_items(self, items):
        """
        Display the list of items in the GUI.
        """
        self.listbox.clear()
        for item in items:
            self.listbox.addItem(item)

    def show_error(self, message):
        """
        Show an error message to the user.
        """
        QMessageBox.critical(self, "Error", message)

    def clear_item_text(self):
        """
        Clear the input box.
        """
        self.input_box.clear()

    def get_item_text(self):
        """
        Get the text from the input box.

        Returns:
            str: Text entered by the user.
        """
        return self.input_box.text()

    def close_application(self):
        """
        Close the application.
        """
        self.close()

    def run(self):
        """
        Run the GUI event loop.
        """
        self.show()
