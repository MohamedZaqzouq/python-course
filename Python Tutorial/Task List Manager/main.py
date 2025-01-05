import os

TASK_FILE = 'tasks.txt'

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def remove_task(tasks):
    task = input("Enter the task to remove: ")
    if task in tasks:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\nTask List Manager")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting Task List Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()