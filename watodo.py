#!/usr/bin/env python3

from rich.console import Console
from rich.table import Table
import json
import sys
import os

DATABASE_LOC = os.path.expanduser("~") + "/.config/watodo"
DATABASE = DATABASE_LOC + "/watodo.json"

class Utils:
    def __init__(self) -> None:
        pass

    def create_template(self):
        template = {
            "in-progress": [],
            "completed": []
        }

        os.makedirs(DATABASE_LOC, exist_ok=True)

        with open(DATABASE, "w") as file:
            json.dump(template, file, indent=4)

    def load_json(self, json_file):
        with open(json_file, "r") as file:
            return json.load(file)


class Todo_Database(Utils):
    def __init__(self) -> None:
        if not os.path.exists(DATABASE):
            self.create_template()

    def add(self, task) -> None:
        with open(DATABASE, "r") as file:
            todos = json.load(file)

        todos["in-progress"].append(task)

        with open(DATABASE, "w") as file:
            json.dump(todos, file, indent=4)

    def complete(self, sno_task) -> None:
        with open(DATABASE, "r") as file:
            todos = json.load(file)

        try:
            completed_task = todos["in-progress"].pop(sno_task - 1)

            todos["completed"].append(completed_task)

            with open(DATABASE, "w") as file:
                json.dump(todos, file, indent=4)
        except IndexError:
            # Just ignore, no need to force any user interaction
            pass

    def show(self, history=False) -> None:
        todos = self.load_json(DATABASE)
        table = Table()
        table.add_column("Just Do It", justify="center",
                         style="cyan", no_wrap=True)
        for todo in todos["in-progress"]:
            table.add_row(todo)

        console = Console()
        console.print(table)

        if (history):
            table = Table()
            todos = self.load_json(DATABASE)
            table = Table()
            table.add_column("That's What I Did?", justify="center",
                            style="cyan", no_wrap=True)
            for todo in todos["completed"]:
                table.add_row(todo)

            console = Console()
            console.print(table)


if __name__ == "__main__":
    args = sys.argv

    if len(args) == 1:
        Todo_Database().show()
        exit(0)

    if args[1] == "c" or args[1] == "a" or args[1] == "h":
        if args[1] == "a":
            task = " ".join(i for i in args[2:])
            Todo_Database().add(task)
        elif args[1] == "c":
            try:
                sno_task = int(args[2])
                Todo_Database().complete(sno_task)
            except ValueError:
                pass
        elif args[1] == "h":
            Todo_Database().show(True)
        else:
            pass
    else:
        pass