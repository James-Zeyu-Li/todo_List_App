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
            try:
                index = int(user_action[5:]) - 1

                items = Todo.current_item()
                if 0 <= index < len(items):
                    new_item = input(
                        f"Change {items[index+1].strip()} to: ") + '\n'
                    Todo.edit_item(index, new_item)
                else:
                    print(
                        f"The number must be between 1 and {len(items)}")

            except ValueError:
                print("The entry is not valid, edit (item_number)")
                continue

        elif user_action.startswith("complete"):
            try:
                item_number = int(user_action[9:])
                index_number = item_number - 1
                removed_item = Todo.mark_complete(index_number)
                message = (
                    f"{item_number} {removed_item} was removed from the list")
                print(message)
            except IndexError:
                print("The number of item you entered does not exist")
                continue

        elif user_action.startswith("exit"):
            status = "exit"

        else:
            print("Invalid enter, please enter (add, show, or exit)")


if __name__ == "__main__":
    main()
