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
    