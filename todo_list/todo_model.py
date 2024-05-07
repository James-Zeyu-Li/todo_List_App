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

