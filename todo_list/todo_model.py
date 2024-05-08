import os


class Todo:
    """
    This is a class for the todo list which allow basic functionalities for users to
    adds, show edits, remove items from the to do list
    save the todo list items in a txt file and read from the file
    """

    def __init__(self, filename='todo_list/todo_list.txt'):
        """
        initiate a todo list to load from the assigned txt file

        args:
            filename (str): to read and update the todo item from the file from
                            the designated file location.
        """
        self.filename = filename
        self.todo_list = []
        self.load_items()

    def load_items(self):
        """
        read the file and check if there are any items already in the txt,
        if so, add it to the list.
        """
        if not os.path.exists(self.filename):
            self.todo_list = []
            self.save_item()
        else:
            with open('todo_list/todo_list.txt', 'r') as file:
                self.todo_list = file.readlines()

    def save_item(self):
        """
        Save user input after add item, edit and mark complete so the code
        won't duplicate.
        """
        with open(self.filename, 'w') as file:
            file.writelines(self.todo_list)

    def add_item(self, item):
        """
        This function allow user to add a new item to the list, save to the
        file by save_item
        """
        self.todo_list.append(item + "\n")
        self.save_item()

    def current_item(self):
        """
        This function return all current items in the todo_list
        """
        return self.todo_list

    def edit_item(self, index, new_item):
        """
        This function allow the user to edit an item after being added to
        the todo list

        Args:
            index: the index of item that the user wants to update.
            new_item: what the user wants to update the item to.

        Return (boolean): true if index within the rage, false other wise
        """
        if 0 <= index < len(self.todo_list):
            self.todo_list[index] = new_item + "\n"
            self.save_input()
            return True
        return False

    def mark_complete(self, index):
        """
        This function allow user to delete/mark complete
        an item from the todo list

        Args: index(int): The index of item in list to be removed.

        Return:the item to be removed

        Raise: IndexError if out of range.

        """
        if 0 <= index < len(self.todo_list):
            item_to_be_removed = self.todo_list.pop(index)
            self.save_item()
            return item_to_be_removed
        else:
            raise IndexError(
                f"The index is out of range, 0 - {len(self.todo_list)}")
