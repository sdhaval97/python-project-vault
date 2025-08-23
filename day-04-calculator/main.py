import os

def clear_screen():
    """Clears the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def add(n1, n2):
    """Returns the sum of 2 numbers"""
    return n1 + n2

def subtract(n1, n2):
    """Returns the difference between the 2 numbers"""
    return n1 - n2

def multiply(n1, n2):
    """Returns the product of 2 numbers"""
    return n1 * n2

def divide(n1, n2):
    """Returns the division of 2 numbers. Handles division by zero"""
    if n2 == 0:
        return "Error: Division by zero is not allowed."
    return n1/n2

def get_number(prompt):
    """Gets valid input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")