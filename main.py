import tasks
# import json
# a = tasks.Task({"name": "Task 1", "priority": "normal", "deadline": None, "description": None})
a = tasks.create_task("Task 1")
print(a)

# tasks.add_task(tasks.Task("Task 1"))
# with open("tasks.json", "w") as file:
#     json.dump(tasks.tasks, file, default=lambda x: x.__dict__)

# tasks.clear_tasks()
# print(tasks.tasks)

# # tasks.tasks = json.loads(js)
# print(tasks.tasks)
