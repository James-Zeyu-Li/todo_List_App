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

    def save_item(self):
        """
        Save user input after add item, edit and mark complete so the code
        won't duplicate.
        """
        with open(self.filename, 'w') as file:
            file.writelines(self.todo_list)

    def add_item(self):
        """
        This function allow user to add a new item to the list, save to the
        file by save_item
        """
        todo = input("Enter a Note: \n") + '\n'
        self.todo_list.append(todo)
        self.save_item()

    def show_item(self):
        """
        This function show all the item in the todo list with a index number
        in the beginning
        """

    def edit_item(self):
        """
        This function allow the user to edit an item after being added to
        the todo list
        """

    def mark_complete(self):
        """
        This function allow user to delete/mark complete
        an item from the todo list
        """
