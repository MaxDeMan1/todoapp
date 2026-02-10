import sys
import tasks
import json
import typing


def main():
    # Loads the saved tasks
    with open("tasks.json", "r") as file:
        tasks.tasks = json.load(file)

    while True:
        # TODO: Wrap grapping input in try/except
        user_input: str = input("Enter command (? for help): ")
        split_input: typing.List[str] = user_input.split()
        match split_input[0]:
            case "?":
                print(
                    "?\t\t\tHelp (this screen)"
                    "\nadd <name> <priority>\tAdds task"
                    "\nremove <name>\t\tRemoves the specified task based on name"
                    "\nclear\t\t\tRemoves all tasks"
                    "\nshow <name>\t\tShows info about the task"
                    "\nlist\t\t\tShows all tasks"
                    "\nExit with ctrl+c"
                )
            case "add":
                name = split_input[1]
                tasks.add_task(tasks.create_task(name))
            case "remove":
                name = split_input[1]
                tasks.remove_task_name(name)
            case "clear":
                tasks.clear_tasks()
            case "show":
                print(tasks.show_task_name(split_input[1]))
            case "list":
                for task in tasks.tasks:
                    print(tasks.show_task(task))
            case _:
                print("Unknown command")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:  # ctrl+c
        # Saves the curent tasks
        with open("tasks.json", "w") as file:
            json.dump(tasks.tasks, file, default=lambda x: x.__dict__)
        print()  # Print newline
        exit(0)
