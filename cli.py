import json
import os

TASK_FILE = "tasks.json"

# Load tasks from a file
def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    return []

# Save tasks to a file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks, description):
    task = {"description": description, "completed": False}
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added.")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\n📋 Your Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["completed"] else "❌"
        print(f"{i}. {task['description']} [{status}]")

# Mark a task as complete
def complete_task(tasks, task_num):
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1]["completed"] = True
        save_tasks(tasks)
        print("🎉 Task marked as completed.")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(tasks, task_num):
    if 0 < task_num <= len(tasks):
        removed = tasks.pop(task_num - 1)
        save_tasks(tasks)
        print(f"🗑️ Task '{removed['description']}' deleted.")
    else:
        print("Invalid task number.")

# Menu for the CLI
def menu():
    tasks = load_tasks()
    while True:
        print("\n===== TaskTrack - CLI Task Manager =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == "1":
            desc = input("Enter task description: ")
            add_task(tasks, desc)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_tasks(tasks)
            try:
                num = int(input("Enter task number to complete: "))
                complete_task(tasks, num)
            except ValueError:
                print("Invalid input.")
        elif choice == "4":
            view_tasks(tasks)
            try:
                num = int(input("Enter task number to delete: "))
                delete_task(tasks, num)
            except ValueError:
                print("Invalid input.")
        elif choice == "5":
            print("👋 Exiting TaskTrack.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    menu()
