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
            
def get_operation():
    """Get a valid operation from the user"""
    while True:
        op = input("Choose an operation (+, -, *, /)").strip()
        if op in ['+', '-', '*', '/']:
            return op
        else:
            print("Invalid operation. Please choose from (+, -, *, /).")

def main():
    """Main application controller for the calculator"""
    while True:
        clear_screen()
        print("🧮 Simple Python Calculator 🧮")
        print("="*30)
        
        num1 = get_number("Enter the first number")
        op = get_operation()
        num2 = get_number("Enter the second number")
        
        result = None
        if op == "+":
            result = add(num1, num2)
        elif op == "-":
            result = subtract(num1, num2)
        elif op == "*":
            result = multiply(num1, num2)
        elif op == "/":
            result = divide(num1, num2)
            
        print("\n" + "-"*30)
        
        # Check if result is a string (zerodivision error)
        if isinstance(result, str):
            print(f"Result: {result}")
        else:
            print(f"{num1} {op} {num2} = {result}")
        print("-"*30)
        
        while True:
            again = input("\nPerform another calculation? (y/n): ").lower().strip()
            if again in ['y', 'yes', 'n', 'no']:
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        
        if again in ['n', 'no']:
            print("\nThanks for using the calculator! 👋")
            break

if __name__ == "__main__":
    main()