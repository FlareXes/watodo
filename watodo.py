#!/usr/bin/env python3

import json
import os
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

        print("\n########## JUST DO IT ##########")
        for i, todo in enumerate(todos["in-progress"]):
            print(f"{i + 1}. {todo}")
        if history:
            print("\n\n########## YOU DID IT! ##########")
            for i, todo in enumerate(todos_history["completed"]):
                print(f"{i + 1}. {todo}")


if __name__ == "__main__":
    config_check()
    # Watodo().add("one")
    # Watodo().done(2)


