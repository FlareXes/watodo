#!/usr/bin/env python3

from ast import arg
import json
import sys
import os


class Utils:
    def __init__(self) -> None:
        pass

    def create_template(self):
        template = {
            "in-progress": [],
            "completed": []
        }

        with open("watodo.json", "w") as file:
            json.dump(template, file, indent=4)


class Todo_Database(Utils):
    def __init__(self) -> None:
        if not os.path.exists("watodo.json"):
            self.create_template()

    def add(self, task) -> None:
        with open("watodo.json", "r") as file:
            todos = json.load(file)
        
        todos["in-progress"].append(task)

        with open("watodo.json", "w") as file:
            json.dump(todos, file, indent=4)

    def complete(self, sno_task) -> None:
        with open("watodo.json", "r") as file:
            todos = json.load(file)

        try:
            completed_task = todos["in-progress"].pop(sno_task - 1)
            
            todos["completed"].append(completed_task)

            with open("watodo.json", "w") as file:
                json.dump(todos, file, indent=4)
        except IndexError:
            # Just ignore, no need to force any user interaction
            pass



if __name__ == "__main__":
    args = sys.argv
    if args[1] == "c" or args[1] == "a":
        if args[1] == "a":
            task = " ".join(i for i in args[2:])
            Todo_Database().add(task)
        elif args[1] == "c":
            try:
                sno_task = int(args[2])
                Todo_Database().complete(sno_task)
            except ValueError:
                pass
        else:
            pass
    else:
        pass