import os

# Function to add tasks to the list
def add_task(task, task_list):
    task_list.append(task)
    print(f"Task added: {task}")

# Function to remove completed tasks
def remove_task(task, task_list):
    try:
        task_list.remove(task)
        print(f"Task removed: {task}")
    except ValueError:
        print("Task not found in the list.")

# Function to view the current task list
def view_tasks(task_list):
    if not task_list:
        print("Your task list is empty.")
    else:
        print("Current tasks:")
        for idx, task in enumerate(task_list, 1):
            print(f"{idx}. {task}")

# Function to save tasks to a file
def save_tasks_to_file(task_list, filename="tasks.txt"):
    try:
        with open(filename, "w") as file:
            for task in task_list:
                file.write(task + "\n")
        print("Tasks have been saved successfully.")
    except Exception as e:
        handle_exception(e)

# Function to load tasks from a file
def load_tasks_from_file(filename="tasks.txt"):
    task_list = []
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                task_list = [line.strip() for line in file.readlines()]
            print("Tasks have been loaded successfully.")
        except Exception as e:
            handle_exception(e)
    else:
        print("No previous tasks found.")
    return task_list

# Function to handle exceptions for file read/write errors
def handle_exception(exception):
    print(f"An error occurred: {exception}")
    # Optionally, log the error or take other actions
    print("Please try again.")

# Main Program to demonstrate task manager functionality
def main():
    task_list = load_tasks_from_file()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Save and Exit")
        choice = input("Choose an option (1/2/3/4): ")

        if choice == "1":
            task = input("Enter the task to add: ")
            if task =="":
                print("Task cannot be empty")
            else:
              add_task(task, task_list)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            remove_task(task, task_list)
        elif choice == "3":
            view_tasks(task_list)
        elif choice == "4":
            save_tasks_to_file(task_list)
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()