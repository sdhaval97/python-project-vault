import os
import time

TASKS_FILE = 'tasks.txt'

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_tasks():
    """Loads tasks from the tasks file. Creates the file if doesn't exist"""
    if not os.path.exists(TASKS_FILE):
        return[]
    try:
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            tasks = [line.strip() for line in f.readlines()]
        return tasks
    except Exception as e:
        print("An error occured while loading tasks: {e}")
        return []

def save_tasks(tasks):
    """Saves the current list of tasks to the file."""
    try:
        with open(TASKS_FILE, 'w', encoding = 'utf-8') as f:
            for task in tasks:
                f.write(task + "\n")
    except Exception as e:
        print(f"An error occured while saving tasks: {e}")

def view_tasks(tasks):
    """Displays all the tasks."""
    clear_screen()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("📝      YOUR TASKS      📝")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    if not tasks:
        print("\nYour to-do list is empty. Use '2' to add a task!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"  {i}. {task}")
    print("\n" + "~"*26)
    input("\nPress Enter to return to the menu...")
    
def add_task(tasks):
    """Adds a new task to the list"""
    clear_screen()
    print("--- Add a New Task ---")
    new_task = input("Enter the task description: ").strip()
    
    if new_task:
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"\n✅ Task '{new_task}' added!")
    else:
        print("\n❌ Task cannot be empty.")
    
    time.sleep(1.5)

def delete_task(tasks):
    """Deletes task from the list."""
    clear_screen()
    print("--- Delete a Task ---")
    
    if not tasks:
        print("Your to-do list is empty. Nothing to delete.")
        time.sleep(2)
        return
    
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print("-----------------------")
    
    try:
        task_num_str = input("Enter the number of the task to delete (or 0 to cancel): ").strip()
        task_num = int(task_num_str)
        
        if task_num == 0:
            print("\nOperation cancelled.")
        elif 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1) # Adjust for 0-based index
            save_tasks(tasks)
            print(f"\n🗑️ Task '{removed_task}' has been deleted.")
        else:
            print("\n❌ Invalid task number.")
    except ValueError:
        print("\n❌ Invalid input. Please enter a number.")
    
    time.sleep(2)

def main():
    """Main application controller."""
    tasks = load_tasks()
    
    while True:
        clear_screen()
        print("==========================")
        print("  Terminal To-Do List")
        print("==========================")
        print("  1. View Tasks")
        print("  2. Add Task")
        print("  3. Delete Task")
        print("  4. Exit")
        print("--------------------------")
        
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("\nSaving tasks... Goodbye! 👋")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")
            time.sleep(1)

if __name__ == "__main__":
    main()
        