tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "status": "Pending"})
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for i in range(len(tasks)):
        print(f"{i + 1}. {tasks[i]['task']} - {tasks[i]['status']}")

def mark_completed():
    view_tasks()
    if not tasks:
        return

    choice = int(input("Enter task number to mark as completed: ")) - 1
    if 0 <= choice < len(tasks):
        tasks[choice]["status"] = "Completed"
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    if not tasks:
        return

    choice = int(input("Enter task number to delete: ")) - 1
    if 0 <= choice < len(tasks):
        tasks.pop(choice)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

while True:
    print("\nTO-DO LIST")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
