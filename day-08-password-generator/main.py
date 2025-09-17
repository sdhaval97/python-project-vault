import string
import secrets
import os
import time

def clear_screen():
    """Clears the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')