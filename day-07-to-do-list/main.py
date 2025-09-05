import os
import time

TASKS_FILE = 'tasks.txt'

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')
    