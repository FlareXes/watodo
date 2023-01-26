#!/usr/bin/env python3

import json
import os
import sys
from platform import system

USER_HOME_DIR = os.path.expanduser("~")

if system() == "Windows":
    DATABASE_DIR = os.path.join(os.getenv("APPDATA"), "watodo")
elif system() == "Darwin":
    DATABASE_DIR = os.path.join(USER_HOME_DIR, "Library", "Application Support" "watodo")
else:
    DATABASE_DIR = os.path.join(USER_HOME_DIR, ".local", "share", "watodo")

CURRENT_DATABASE = os.path.join(DATABASE_DIR, "watodo-current.json")
HISTORY_DATABASE = os.path.join(DATABASE_DIR, "watodo-history.json")


def help():
    print("""\033[96mUSAGE: watodo [Option] (a, c, h, reset, help) { todo }

Arguments:\033[00m
    \033[92ma 	    Add a todo\033[00m
    \033[92mc 	    Mark todo as complete\033[00m
    \033[93mh 	    Show todos with history\033[00m
    \033[91mreset   Forget all todos including history\033[00m

\033[96m# Add a todo\033[00m
watodo a [my todo]

\033[96m# Mask as complete a todo\033[00m
watodo c [todo sno.]

\033[96m# Show all todo with history\033[00m
watodo h

\033[96m# Delete all todo with history\033[00m
watodo reset
""")


def config_check():
    os.makedirs(DATABASE_DIR, exist_ok=True)

    if not os.path.exists(CURRENT_DATABASE):
        template = {"in-progress": [], }
        with open(CURRENT_DATABASE, "w") as f:
            json.dump(template, f, indent=4)

    if not os.path.exists(HISTORY_DATABASE):
        template = {"completed": [], }
        with open(HISTORY_DATABASE, "w") as f:
            json.dump(template, f, indent=4)


class Utils:
    def __init__(self, filename):
        self.filename = filename

    def load_json(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def dump_json(self, todos):
        with open(self.filename, "w") as f:
            json.dump(todos, f, indent=4)

    @staticmethod
    def pprint(id: int = None, todo: str = None):
        if id and todo:
            todo = repr(todo).replace("'", "")
            print(f"\033[92m\033[1m{id} >\033[0m\033[00m \033[3;1m{todo}\033[00m")
        elif todo:
            print(f"\033[96m\033[1m{todo}\033[0m\033[00m")


class Watodo:
    def __init__(self):
        pass

    def add(self, todo):
        todos = Utils(CURRENT_DATABASE).load_json()
        todos["in-progress"].append(todo)
        Utils(CURRENT_DATABASE).dump_json(todos)
        return True

    def done(self, sno):
        todos = Utils(CURRENT_DATABASE).load_json()
        todos_history = Utils(HISTORY_DATABASE).load_json()
        try:
            done_todo = todos["in-progress"].pop(sno - 1)
            Utils(CURRENT_DATABASE).dump_json(todos)

            todos_history["completed"].append(done_todo)
            Utils(HISTORY_DATABASE).dump_json(todos_history)
            return True
        except IndexError:
            # Just ignore, no need to force any user interaction
            return False

    def show(self, history: bool = False):
        todos = Utils(CURRENT_DATABASE).load_json()
        todos_history = Utils(HISTORY_DATABASE).load_json()

        print()
        for i, todo in enumerate(todos["in-progress"]):
            Utils.pprint(i + 1, todo)
        if history:
            Utils.pprint(todo="\n\n########## YOU DID IT! ##########")
            Utils.pprint(todo="---------------------------------\n")
            for i, todo in enumerate(todos_history["completed"]):
                Utils.pprint(i + 1, todo)
        print()


if __name__ == "__main__":
    config_check()
    args = sys.argv

    if len(args) == 1:
        Watodo().show()

    elif args[1] == "a" or args[1] == "c" or args[1] == "h" or args[1] == "reset" or args[1] == "help":
        # Add Task
        if args[1] == "a":
            todo = " ".join(i for i in args[2:])
            Watodo().add(todo)

        # Complete Task
        elif args[1] == "c":
            try:
                sno = int(args[2])
            except ValueError:
                sys.exit(2)
            if sno > 0:
                Watodo().done(sno)

        # Show Tasks And History
        elif args[1] == "h":
            Watodo().show(True)

        # Reset Database
        elif args[1] == "reset":
            ans = input("Are you sure you want to delete all tasks and history (y/N)? ").lower()
            if ans == "y":
                try:
                    os.remove(CURRENT_DATABASE)
                    os.remove(HISTORY_DATABASE)
                    print("Successfully deleted tasks and history.")
                except OSError:
                    print("Failed to delete tasks and history.")
            else:
                print("Abort deletion of tasks and history.")
        else:
            help()
    else:
        help()
        sys.exit(2)
