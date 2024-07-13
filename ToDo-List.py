#ToDo List App

def display_menu():
    """Display the menu options to the user."""
    print("""
    Welcome to the To-Do List App!

    Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit
    """)

def add_task(tasks):
    """Add a new task to the to-do list."""
    task_title = input("Enter the task title: ")
    tasks.append({"title": task_title, "status": "Incomplete"})
    print(f'Task "{task_title}" added.\n')

def view_tasks(tasks):
    """Display all tasks with their status."""
    if not tasks:
        print("No tasks in the list.\n")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['title']} - {task['status']}")
    print("")

def mark_task_complete(tasks):
    """Mark a task as complete."""
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]['status'] = "Complete"
            print(f'Task "{tasks[task_number - 1]["title"]}" marked as complete.\n')
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def delete_task(tasks):
    """Delete a task from the to-do list."""
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f'Task "{removed_task["title"]}" deleted.\n')
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Thank you for using the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main()
