"""
This file will be used for a app view, the user will interact with the app
"""

from model.todo_model import Todo
import FreeSimpleGUI as fsg

todo_class = Todo()

label = fsg.Text("Welcome to the To Do List Application")
input_box = fsg.InputText(
    tooltip="Enter an action (1:add, 2:show, 3:edit, 4:complete, 5:exit):",
    key="todo")

add_button = fsg.Button("Add")

# layout every[],[] represent another line
layout = [
    [label],
    [input_box, add_button]]

window = fsg.Window("To Do List APP",
                    layout,
                    font=("Helvetica", 20))


while True:
    event, values = window.read()  # a tuple

    if event == fsg.WINDOW_CLOSED:
        break


window.close()
