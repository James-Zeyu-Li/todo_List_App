"""
This is a practice project to create a to do list application using python.
"""
from todo_model import Todo


def main():

    status = "running"

    while status != "exit":
        user_action = input(
            "Enter an action \
(1:add, 2:show, 3:edit, 4:complete, 5:exit):\n").strip().lower()

        if user_action.startswith("add"):
            item = user_action[4:]
            Todo.add_item(item)
            Todo.save_item()

        elif user_action.startswith("show"):
            items = Todo.current_item()
            for index, item in enumerate(items):
                print(f"{index+1}:{item.strip()}")

        elif user_action.startswith("edit"):

        elif user_action.startswith("complete"):

        elif user_action.startswith("exit"):
            status = "exit"

        else:
            print("Invalid enter, please enter (add, show, or exit)")


if __name__ == "__main__":
    main()
