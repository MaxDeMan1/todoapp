import json
import typing

import tasks


def main() -> None:

    def arg_count_checker(arg_count: int, str_list: typing.List[str]) -> bool:
        """
        Ensures the correct amount of arguments is provided.
        arg_count: int, amount of arguments that should be provided, excluding command.
        Prints that input had wrong arg count and returns false if the arg count is
        not equal to the arg_count. Returns True otherwise.
        """
        if arg_count != (len(str_list) + 1):  # Add 1 to account for command
            print(f"Incorrect argument count (should be {arg_count} arguments)")
            return False
        return True

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
                if len(split_input) < 2 or len(split_input) > 3:
                    print("Incorrect argument count (should be 1 OR 2 argument)")
                    continue
                name: str = split_input[1]
                # If user sets priority, use that else default to normal
                try:
                    priority: str = split_input[2]
                except IndexError:
                    priority = "normal"
                tasks.add_task(
                    tasks.create_task(name, typing.cast(tasks._priority, priority))
                )
            case "remove":
                if arg_count_checker(1, split_input) is False:
                    continue
                name = split_input[1]
                try:
                    tasks.remove_task_name(name)
                except ValueError:
                    print("Task must be in the task list")
            case "clear":
                tasks.clear_tasks()
            case "show":
                if arg_count_checker(1, split_input) is False:
                    continue
                try:
                    print(tasks.show_task_name(split_input[1]))
                except ValueError:
                    print("Task must be in the task list")
            case "list":
                if tasks.get_tasks_count() == 0:
                    print("Task list empty")
                    continue
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
