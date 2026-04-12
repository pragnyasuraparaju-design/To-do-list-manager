from storage.file_handler import load_tasks, save_tasks
from utils import generate_id, format_task, get_current_time

class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self, title):
        try:
            if not title.strip():
                raise ValueError("Task title cannot be empty.")

            task = {
                "id": generate_id(self.tasks),
                "title": title,
                "completed": False,
                "created_at": get_current_time()
            }

            self.tasks.append(task)
            save_tasks(self.tasks)
            print("✅ Task added successfully!")

        except ValueError as ve:
            print(f"Error: {ve}")

    def view_tasks(self):
        if not self.tasks:
            print("📭 No tasks found.")
            return

        for task in self.tasks:
            print(format_task(task))

    def complete_task(self, task_id):
        try:
            for task in self.tasks:
                if task["id"] == task_id:
                    task["completed"] = True
                    save_tasks(self.tasks)
                    print("🎉 Task marked as completed!")
                    return

            raise LookupError("Task not found.")

        except LookupError as le:
            print(f"Error: {le}")

    def delete_task(self, task_id):
        try:
            new_tasks = [t for t in self.tasks if t["id"] != task_id]

            if len(new_tasks) == len(self.tasks):
                raise LookupError("Task not found.")

            self.tasks = new_tasks
            save_tasks(self.tasks)
            print("🗑 Task deleted!")

        except LookupError as le:
            print(f"Error: {le}")
