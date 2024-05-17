from PyQt5.QtWidgets import (QWidget, QVBoxLayout,
                             QLabel, QPushButton, QLineEdit, QListWidget,
                             QMessageBox, QInputDialog)


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

        # Main layout
        self.main_layout = QVBoxLayout()

        # Label
        self.label = QLabel("Welcome to the To Do List Application")
        self.main_layout.addWidget(self.label)
