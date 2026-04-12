from manager import TaskManager

def show_menu():
    print("\n📌 TO-DO LIST MENU")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


def main():
    manager = TaskManager()

    while True:
        show_menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                title = input("Enter task title: ")
                manager.add_task(title)

            elif choice == 2:
                manager.view_tasks()

            elif choice == 3:
                task_id = int(input("Enter task ID: "))
                manager.complete_task(task_id)

            elif choice == 4:
                task_id = int(input("Enter task ID: "))
                manager.delete_task(task_id)

            elif choice == 5:
                print("👋 Goodbye!")
                break

            else:
                print("⚠️ Invalid choice.")

        except ValueError:
            print("⚠️ Please enter a valid number.")

        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
