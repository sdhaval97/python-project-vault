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
    