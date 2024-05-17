# To-Do List Application

This is a practice project to create a to-do list application using Python and PyQt5. The application implements the Model-View-Controller (MVC) design pattern to separate concerns and improve maintainability.

## Features

- Add, edit, and remove to-do items.
- Mark items as complete / delete an item.
- Save and load to-do items from a .txt file.
- Graphical user interface (GUI) built with PyQt5.

## Getting Started

### Run the executable directly

- On macOS/Linux:
    - Double Click to run (work on some systems)
    - run the 

    ```sh
    .../todo_List_App/TodoApp
    ```

- On Windows:
    - Navigate to the dist/TodoApp/ directory and double-click the TodoApp.exe file.

### Prerequisites on running the python file directly

- Python 3.x
- PyQt5

### Installation

1. Clone the repository:

```sh
git clone https://github.com/your-username/todo-list-app.git
cd todo-list-app
```

2. Install the required dependencies:

```sh
pip install pyqt5
```

### Running the Application
To start the application, run the main.py file:

```sh
python main.py
```

## Project Structure
```
todo-list-app/
│
├── controller/
│   └── todo_controller.py   # Controller handling logic between model and view
│
├── model/
│   └── todo_model.py        # Model handling data and business logic
│
├── view/
│   └── todo_GUI.py          # View handling graphical user interface
│
├── todo_list/
│   └── todo_list.txt        # Text file storing to-do items
│
├── main.py                  # Main entry point of the application
├── TodoApp.exec             # This is the executable
└── README.md                # Project documentation
```

#### Usage
- Launch the application by running main.py or the generated executable.
- Enter your to-do item in the input box and click "Add".
- To edit an item, select it from the list and click "Edit".
- To mark an item as complete, select it from the list and click "Complete".
- The list of to-do items will be saved to and loaded from todo_list.txt.
