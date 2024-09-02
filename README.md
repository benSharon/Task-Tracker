
# Task Tracker

A command-line tool for managing tasks with functionalities to add, update, list, delete, and mark tasks. Tasks are stored in a JSON file, and the tool provides a simple way to track the status of tasks such as "todo," "in-progress," and "done."

## Features

- **Add Tasks**: Add new tasks to your task list.
- **Update Tasks**: Update the description of existing tasks.
- **List Tasks**: Display all tasks or filter them by status (`todo`, `in-progress`, `done`).
- **Mark Tasks**: Mark tasks as `in-progress` or `done`.
- **Delete Tasks**: Remove tasks from your list.

## Requirements

- Python 3.x
- `argparse` (comes with the Python standard library)
- `prettytable` (for displaying tasks in a table format)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/task-tracker.git
   cd task-tracker
   ```

2. Install the required dependencies:

   ```bash
   pip install prettytable
   ```

## Usage

Run the script from the command line:

```bash
python tracker_cli.py [command] [arguments]
```

### Example Usages:

- **Add a Task**:
  ```bash
  python tracker_cli.py add "Buy groceries"
  ```

- **Update a Task**:
  ```bash
  python tracker_cli.py update 1 "Buy groceries and cook dinner"
  ```

- **Mark a Task as In-Progress**:
  ```bash
  python tracker_cli.py mark-in-progress 1
  ```

- **Mark a Task as Done**:
  ```bash
  python tracker_cli.py mark-done 1
  ```

- **Delete a Task**:
  ```bash
  python tracker_cli.py delete 1
  ```

- **List All Tasks**:
  ```bash
  python tracker_cli.py list
  ```

- **List Tasks by Status**:
  ```bash
  python tracker_cli.py list done
  python tracker_cli.py list todo
  python tracker_cli.py list in-progress
  ```

### Example output:
```
PS C:\Users\path\to\yout\project> python .\tracker_cli.py list
+----+---------------------+-------------+---------------------+---------------------+
| id |     description     |    status   |      createdAt      |      updatedAt      |
+----+---------------------+-------------+---------------------+---------------------+
| 1  |  go have breakfast  |     done    | 2024-09-01 13:30:59 | 2024-09-01 13:31:36 |
+----+---------------------+-------------+---------------------+---------------------+
| 2  |        series       | in-progress | 2024-09-01 13:31:07 | 2024-09-01 13:31:48 |
+----+---------------------+-------------+---------------------+---------------------+
| 3  | polish task-tracker |     todo    | 2024-09-01 13:31:11 | 2024-09-01 13:47:35 |
+----+---------------------+-------------+---------------------+---------------------+
| 4  |        class        |     todo    | 2024-09-01 14:15:29 |                     |
+----+---------------------+-------------+---------------------+---------------------+
```
### Help

To see the help message:

```bash
python tracker_cli.py -h
```
```python
PS C:\Users\path\to\your\project> python .\tracker_cli.py --help

usage: python tracker_cli.py [-h] [add TASK] | [mark-in-progress [ID...]] | [mark-done [ID...]] | [list done | todo | in-progress] | [update ID TASK]

Command-line tool to add, update, list, delete and mark tasks.

positional arguments:
  {add,update,mark-in-progress,mark-done,delete,list}
    add                 add a task
    update              update an existing task (task_id [int] and task_update [str])
    mark-in-progress    mark a task (or several tasks) as 'in-progress'
    mark-done           mark a task (or several tasks) as 'done'
    delete              delete a task
    list                list task(s) [todo | done | in-progress]

options:
  -h, --help            show this help message and exit

    Example usages:
        python tracker_cli.py add "Buy groceries"  (ID: 1)
        python tracker_cli.py add "Visit family"   (ID: 2)
        python tracker_cli.py add "Gas car"        (ID: 3)

        python tracker_cli.py update 1 "Buy groceries and cook dinner"
        python tracker_cli.py delete 1

        python tracker_cli.py mark-in-progress 1
        python tracker_cli.py mark-in-progress 1 2 3
        python tracker_cli.py mark-done 1
        python tracker_cli.py mark-done 1 2 3

        python tracker_cli.py list
        python tracker_cli.py list done
        python tracker_cli.py list todo
        python tracker_cli.py list in-progress
```

## Project Structure

- `tracker_cli.py`: The entry point of the application, responsible for parsing command-line arguments and invoking the appropriate task functions.
- `manager.py`: Contains functions for task operations like adding, updating, listing, marking, and deleting tasks.
- `json_manager.py`: Manages reading from and writing to the JSON file where tasks are stored.

## JSON File

The tasks are stored in a JSON file named `tasks.json` in the same directory as the script. The file will be created automatically if it doesn't exist via `add_task` method.

## Contributing

Feel free to submit issues, fork the repository, and send pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Project URL
https://roadmap.sh/projects/task-tracker
