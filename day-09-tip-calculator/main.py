import os
import time

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
def get_numeric_input(prompt, input_type=float):
    """Generic function to get and validate numeric input."""
    while True:
        try:
            value_str = input(prompt).strip()
            value = input_type(value_str)
            if value > 0:
                return value
            else:
                print("❌ Please enter a positive number greater than zero.")
        except ValueError:
            print(f"❌ Invalid input. Please enter a valid {'number' if input_type is float else 'integer'}.")