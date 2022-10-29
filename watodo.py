#!/usr/bin/env python3

from secrets import choice
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
        
        table.add_column("    Just Do It", justify="left", style="cyan", no_wrap=True, header_style="white")

        for i, todo in enumerate(todos["in-progress"]):
            table.add_row(f"[magenta]{str(i + 1)}[/ magenta] [bold white]>[/bold white] {todo}")

        console = Console()
        console.print(table)

        # To Show History Also #
        if (history):
            todos = self.load_json(DATABASE)
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
        exit(0)

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
            console.print("[yellow]WARNING![/yellow] This will remove all the tasks (y/N): ", end="")
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
