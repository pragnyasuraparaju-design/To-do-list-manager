import os

TASKS_FILE = "tasks_data.py"


def load_tasks():
    try:
        if os.path.exists(TASKS_FILE):
            import tasks_data
            return tasks_data.tasks
    except Exception:
        pass
    return []


def save_tasks(tasks):
    try:
        with open(TASKS_FILE, "w") as f:
            f.write("tasks = ")
            f.write(repr(tasks))
    except IOError as e:
        print(f"Error saving tasks: {e}")
