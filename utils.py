from datetime import datetime

def generate_id(tasks):
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def format_task(task):
    status = "✔" if task["completed"] else "✘"
    return f"[{status}] {task['id']} - {task['title']} (Created: {task['created_at']})"


def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
