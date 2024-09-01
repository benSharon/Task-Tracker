import pathlib

from json_manager import read_json, write_to_json, clear_json, display_json
from datetime import datetime

time_now = datetime.today().strftime("%Y-%m-%d %H:%M:%S")


def add_task(task_description: str):
    task_id = 1
    task = [
        {
            "id": task_id,
            "description": task_description,
            "status": "todo",
            "createdAt": time_now,
            "updatedAt": "",
        }
    ]
    if not pathlib.Path("../tasks.json") or pathlib.Path("../tasks.json").stat().st_size == 0:
        write_to_json(task, "../tasks.json", "w")
        print(f'Task {task_id} "{task_description}" has been added successfully.')
    else:
        tasks_data: list[dict] = read_json("../tasks.json")

        # Clearing json file of any data.
        clear_json("../tasks.json")

        # Get last task's id.
        last_id = max(task["id"] for task in tasks_data) if tasks_data else 0

        new_task = {
            "id": last_id + 1,
            "description": task_description,
            "status": "todo",
            "createdAt": time_now,
            "updatedAt": "",
        }
        tasks_data.append(new_task)
        write_to_json(tasks_data, "../tasks.json", "a")
        print(f'Task {task_id} "{task_description}" has been added successfully.')


def update_task(task_id: int, new_task_description: str):
    if not pathlib.Path("../tasks.json"):
        raise FileNotFoundError("'tasks.json' does not exist.")
    else:
        tasks_data: list[dict] = read_json("../tasks.json")
        task_found = False
        for task in tasks_data:
            if task["id"] == task_id:
                task_found = True
                task["description"] = new_task_description
                task["updatedAt"] = time_now

        if task_found:
            # Clearing json file of any data
            clear_json("../tasks.json")
            write_to_json(tasks_data, "../tasks.json", "w")
            print(f"Task {task_id} has been updated successfully at {time_now}.")
        else:
            print(f"Task {task_id} not found.")


def mark_in_progress(task_id: int):
    if not pathlib.Path("../tasks.json"):
        raise FileNotFoundError("'tasks.json' does not exist.")
    else:
        tasks_data: list[dict] = read_json("../tasks.json")
        task_found = False
        for task in tasks_data:
            if task["id"] == task_id:
                task_found = True
                task["status"] = "in-progress"
                task["updatedAt"] = time_now

        if task_found:
            # Clearing json file.
            clear_json("../tasks.json")
            write_to_json(tasks_data, "../tasks.json", "w")
            print(f"Task {task_id} has been marked 'in-progress'.")
        else:
            print(f"Task {task_id} not found.")


def mark_done(task_id: int):
    if not pathlib.Path("../tasks.json"):
        raise FileNotFoundError("'tasks.json' does not exist.")
    else:
        tasks_data: list[dict] = read_json("../tasks.json")
        task_found = False
        for task in tasks_data:
            if task["id"] == task_id:
                task_found = True
                task["status"] = "done"
                task["updatedAt"] = time_now

        if task_found:
            # Clearing json file.
            clear_json("../tasks.json")
            write_to_json(tasks_data, "../tasks.json", "w")
            print(f"Task {task_id} has been marked as 'done'.")
        else:
            print(f"Task {task_id} not found.")


def delete_task(task_id: int):
    if not pathlib.Path("../tasks.json"):
        raise FileNotFoundError("'tasks.json' does not exist.")
    else:
        tasks_data: list[dict] = read_json("../tasks.json")
        task_found = False
        for task in tasks_data:
            if task["id"] == task_id:
                task_found = True
                tasks_data.remove(task)

        if task_found:
            # Clearing json file.
            clear_json("../tasks.json")
            write_to_json(tasks_data, "../tasks.json", "w")
            print(f"Task {task_id} has been removed successfully.")
        else:
            print(f"Task {task_id} not found.")


def list_task(status: str):
    if not pathlib.Path("../tasks.json"):
        raise FileNotFoundError("'tasks.json' does not exist.")
    else:
        display_json(status)
