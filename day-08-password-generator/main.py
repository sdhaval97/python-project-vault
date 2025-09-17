import string
import secrets
import os
import time

def clear_screen():
    """Clears the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')
    
def get_password_specs():
    """Gets password length and character type preferences from the user."""
    clear_screen()
    print("===================================")
    print("  Secure Password Generator")
    print("===================================")
    
    # Get password length
    while True:
        try:
            length_str = input("Enter the desired password length (8-64): ").strip()
            length = int(length_str)
            if 8 <= length <= 64:
                break
            else:
                print("❌ Invalid length. Please enter a number between 8 and 64.")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
                