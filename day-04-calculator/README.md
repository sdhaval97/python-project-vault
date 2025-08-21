# Project 4: Crafting a Simple Calculator

## Project Overview
A command-line calculator that performs basic arithmetic operations: addition, subtraction, multiplication, and division. This project is a classic exercise in functional decomposition, where each operation is handled by its own dedicated, reusable function.

## What You'll Learn
- **Functional Decomposition**: How to break a problem down into smaller, manageable, and reusable functions.
- **Robust Input Validation**: Writing functions to handle and validate user input to prevent errors.
- **Error Handling**: Specifically addressing edge cases like division by zero.
- **Code Modularity**: Creating clean, testable, and extensible code by isolating logic.
- **Main Application Loop**: Structuring a program to run continuously until the user decides to exit.

## Features
- **Four Basic Operations**: Supports addition (+), subtraction (-), multiplication (*), and division (/).
- **User-Friendly Interface**: A clean and simple command-line interface that guides the user.
- **Input Validation**: Ensures that users enter valid numbers and operators.
- **Division by Zero Protection**: Prevents the program from crashing if the user attempts to divide by zero.
- **Continuous Calculations**: Allows the user to perform multiple calculations without restarting the script.

## How to Run
```bash
python calculator.py
```

## Sample Output
```
🧮 Simple Python Calculator 🧮
==============================
Enter the first number: 50
Choose an operation (+, -, *, /): /
Enter the second number: 0

------------------------------
Result: Error: Division by zero is not allowed.
------------------------------

Perform another calculation? (y/n): y

[Screen Clears]

🧮 Simple Python Calculator 🧮
==============================
Enter the first number: 25
Choose an operation (+, -, *, /): *
Enter the second number: 4

------------------------------
Result: 25.0 * 4.0 = 100.0
------------------------------

Perform another calculation? (y/n): n

Thanks for using the calculator! 👋
```

## Code Structure
- `calculator.py` - The main application file.
- `add()`, `subtract()`, `multiply()`, `divide()`: Individual functions for each arithmetic operation, embodying the principle of functional decomposition.
- `get_number()`: A dedicated function to get and validate numerical input from the user.
- `get_operation()`: A function to get and validate the mathematical operator from the user.
- `main()`: The main controller that runs the application loop and calls the other functions.

## Enhancements (Optional)
- **More Operations**: Add functions for exponentiation (`**`), modulus (`%`), or square root.
- **Scientific Calculator**: Include trigonometric functions (sin, cos, tan).
- **Memory Functions**: Implement M+, MR, and MC (memory add, memory recall, memory clear).
- **GUI Interface**: Build a graphical user interface using a library like Tkinter or PyQt.

## Time Estimate
**Beginner**: 60-90 minutes
**With enhancements**: 3-5 hours

## Key Concepts
- Functional Decomposition
- Input/Output Handling
- Error and Edge Case Management
- Type Casting (string to float)
- Conditional Logic (`if`/`elif`/`else`)
