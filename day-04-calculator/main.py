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
