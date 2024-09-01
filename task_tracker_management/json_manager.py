import json
import pathlib

from prettytable import PrettyTable


def write_to_json(task, json_file_name: str, mode: str):
    with open(json_file_name, mode) as file:
        json.dump(task, file, indent=4)
        file.write("\n")


def read_json(json_file_name: str):
    if pathlib.Path("tasks.json").stat().st_size == 0:
        print("JSON file is empty.")
    else:
        with open(json_file_name, "r") as file:
            return json.load(file)


def clear_json(json_file_name: str):
    open(json_file_name, "w").close()


def display_json(status: str):
    json_data = read_json("tasks.json")
    if not json_data:
        print("No tasks found.")
    else:
        table = PrettyTable()
        if not status:
            table.field_names = [
                "id",
                "description",
                "status",
                "createdAt",
                "updatedAt",
            ]
            for task in json_data:
                table.add_row(
                    [
                        task["id"],
                        task["description"],
                        task["status"],
                        task["createdAt"],
                        task["updatedAt"],
                    ],
                    divider=True,
                )
            if not json_data:
                print("No tasks found.")
            else:
                print(table)

        elif status == "done":
            done_tasks = [task for task in json_data if task["status"] == "done"]
            table.field_names = [
                "id",
                "description",
                "status",
                "createdAt",
                "updatedAt",
            ]
            for task in done_tasks:
                table.add_row(
                    [
                        task["id"],
                        task["description"],
                        task["status"],
                        task["createdAt"],
                        task["updatedAt"],
                    ],
                    divider=True,
                )
            if not done_tasks:
                print('No "done" tasks found.')
            else:
                print(table)

        elif status == "in-progress":
            in_progress_tasks = [
                task for task in json_data if task["status"] == "in-progress"
            ]
            table.field_names = [
                "id",
                "description",
                "status",
                "createdAt",
                "updatedAt",
            ]
            for task in in_progress_tasks:
                table.add_row(
                    [
                        task["id"],
                        task["description"],
                        task["status"],
                        task["createdAt"],
                        task["updatedAt"],
                    ],
                    divider=True,
                )
            if not in_progress_tasks:
                print('No "in-progress" tasks found.')
            else:
                print(table)

        elif status == "todo":
            todo_tasks = [task for task in json_data if task["status"] == "todo"]
            table.field_names = [
                "id",
                "description",
                "status",
                "createdAt",
                "updatedAt",
            ]
            for task in todo_tasks:
                table.add_row(
                    [
                        task["id"],
                        task["description"],
                        task["status"],
                        task["createdAt"],
                        task["updatedAt"],
                    ],
                    divider=True,
                )
            if not todo_tasks:
                print('No "todo" tasks found.')
            else:
                print(table)
