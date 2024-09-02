import argparse

from task_tracker_management.manager import (
    add_task,
    update_task,
    list_task,
    mark_in_progress,
    mark_done,
    delete_task,
)


def main():
    PROG = "Task Tracker"
    DESCRIPTION = "Command-line tool to add, update, list, delete and mark tasks."
    USAGE = (
        "python tracker_cli.py [-h] [add TASK] | [mark-in-progress [ID...]] | [mark-done [ID...]] | "
        "[list done | todo | in-progress] | [update ID TASK]"
    )

    EPILOG = """
    Example usages:
        python tracker_cli.py add "Buy groceries"  (ID: 1)

        python tracker_cli.py update 1 "Buy groceries and cook dinner"
        python tracker_cli.py delete 1

        python tracker_cli.py mark-in-progress 1
        python tracker_cli.py mark-done 1

        python tracker_cli.py list
        python tracker_cli.py list done
        python tracker_cli.py list todo
        python tracker_cli.py list in-progress
    """

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        usage=USAGE,
        prog=PROG,
        description=DESCRIPTION,
        epilog=EPILOG,
    )

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="add a task")
    add_parser.add_argument("task_description", type=str, help="add a task")

    update_parser = subparsers.add_parser(
        "update", help="update an existing task (task_id [int] and task_update [str])"
    )
    update_parser.add_argument("task_id", type=int, help="The ID of the task to update")
    update_parser.add_argument(
        "task_description", type=str, help="The updated version of the existing task"
    )

    mark_in_progress_parser = subparsers.add_parser(
        "mark-in-progress", help="mark a task (or several tasks) as 'in-progress'"
    )
    mark_in_progress_parser.add_argument(
        "task_ids", nargs="+", type=int, help="Task id(s) to mark as 'in-progress'"
    )

    mark_done_parser = subparsers.add_parser(
        "mark-done", help="mark a task (or several tasks) as 'done'"
    )
    mark_done_parser.add_argument(
        "task_ids", nargs="+", type=int, help="Task id(s) to mark as 'done'"
    )

    delete_parser = subparsers.add_parser(
        "delete", help="delete a task (or several tasks)"
    )
    delete_parser.add_argument(
        "task_ids", nargs="+", type=int, help="Task id(s) to be deleted"
    )

    list_parser = subparsers.add_parser(
        "list", help="list task(s) [todo | done | in-progress]"
    )
    list_parser.add_argument(
        "status",
        nargs="?",
        choices=["done", "todo", "in-progress"],
        help="the status of tasks to list",
    )

    args = parser.parse_args()
    if args.command == "add":
        add_task(args.task_description)

    elif args.command == "update":
        update_task(args.task_id, args.task_description)

    elif args.command == "mark-in-progress":
        for task_id in args.task_ids:
            mark_in_progress(task_id)

    elif args.command == "mark-done":
        for task_id in args.task_ids:
            mark_done(task_id)

    elif args.command == "delete":
        for task_id in args.task_ids:
            delete_task(task_id)

    elif args.command == "list":
        list_task(args.status)


if __name__ == "__main__":
    main()
