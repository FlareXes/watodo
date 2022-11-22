#!/usr/bin/env python3

from secrets import choice
from rich.console import Console
from rich.table import Table
from platform import system, getenv
import json
import sys


USER_HOME_DIR = os.path.expanduser("~")

if system() == "Windows":
    DATABASE_DIR = os.path.join(getenv("APPDATA"), "watodo")
elif system() == "Darwin":
    DATABASE_DIR = os.path.join(USER_HOME_DIR, "Library", "Application Support" "watodo")
else:
    DATABASE_DIR = os.path.join(USER_HOME_DIR, ".local", "share", "watodo")

DATABASE = os.path.join(DATABASE_DIR, "watodo.json")


class Utils:
    def __init__(self) -> None:
        pass

    def create_template(self):
        template = {
            "in-progress": [],
            "completed": []
        }

        os.makedirs(DATABASE_DIR, exist_ok=True)

        with open(DATABASE, "w") as file:
            json.dump(template, file, indent=4)

    def load_json(self):
        with open(DATABASE, "r") as file:
            return json.load(file)

    def dump_json(self, todos):
        with open(DATABASE, "w") as file:
            json.dump(todos, file, indent=4)


class Todo_Database(Utils):
    def __init__(self) -> None:
        if not os.path.exists(DATABASE):
            self.create_template()

    def add(self, task) -> None:
        todos = self.load_json()
        todos["in-progress"].append(task)
        self.dump_json(todos)

    def complete(self, sno_task) -> None:
        todos = self.load_json()

        try:
            completed_task = todos["in-progress"].pop(sno_task - 1)
            todos["completed"].append(completed_task)
            self.dump_json(todos)
        except IndexError:
            # Just ignore, no need to force any user interaction
            pass

    def show(self, history=False) -> None:
        todos = self.load_json()
        table = Table()

        table.add_column("    Just Do It", justify="left", style="cyan", no_wrap=True, header_style="white")

        for i, todo in enumerate(todos["in-progress"]):
            table.add_row(f"[magenta]{str(i + 1)}[/ magenta] [bold white]>[/bold white] {todo}")

        console = Console()
        console.print(table)

        # To Show History Also #
        if (history):
            todos = self.load_json()
            table = Table()
            table = Table(show_lines=True)

            table.add_column("S.No.", justify="center", style="cyan", no_wrap=True)
            table.add_column("That's What I Did?", justify="center", style="red", no_wrap=True)

            for i, todo in enumerate(todos["completed"]):
                table.add_row(str(i + 1), todo)

            console = Console()
            console.print(table)


if __name__ == "__main__":
    args = sys.argv
    console = Console()

    if len(args) == 1:
        Todo_Database().show()
        sys.exit(0)

    if args[1] == "c" or args[1] == "a" or args[1] == "h" or args[1] == "reset":
        # Add Task
        if args[1] == "a":
            task = " ".join(i for i in args[2:])
            if task != "":
                Todo_Database().add(task)

        # Complete Task
        elif args[1] == "c":
            try:
                sno_task = int(args[2])
                Todo_Database().complete(sno_task)
                Todo_Database().show()
            except (ValueError, IndexError):
                pass

        # Show Tasks History
        elif args[1] == "h":
            Todo_Database().show(True)

        # Reset Database
        elif args[1] == "reset":
            console.print(
                "[yellow]WARNING![/yellow] This will remove all the tasks (y/N): ", end="")
            choice = input()
            if choice == "y":
                Utils().create_template()
                print("Removed All Tasks Successfully!")
            else:
                print("Process Aborted!")
        else:
            pass
    else:
        pass
