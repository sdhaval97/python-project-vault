# Project 9: Tip Calculator

## Project Overview
A practical command-line tool designed to quickly and accurately calculate the tip for a bill and split the total cost among a number of people. This project focuses on handling numerical inputs, performing arithmetic with floating-point numbers, and formatting the output in a clean, user-friendly way.

## What You'll Learn
- **Arithmetic Operations**: Performing calculations with user-provided numbers.
- **Floating-Point Formatting**: Using f-strings to format currency values to two decimal places (e.g., `:.2f`).
- **Type Casting**: Converting string inputs into numerical types like `float` and `int`.
- **User-Friendly Output**: Presenting calculated data in a clear and readable format.
- **Input Validation**: Ensuring that inputs are positive numbers and handling invalid entries gracefully.

## Features
- **Customizable Inputs**: User can input any bill amount, tip percentage, and number of people.
- **Precise Calculations**: Accurately calculates the tip amount, the total bill, and the share for each person.
- **Clear Results Display**: The output is neatly organized and easy to understand.
- **Robust Input Handling**: Prevents errors from non-numeric or negative inputs.
- **Calculate Again**: A simple loop lets the user perform multiple calculations without restarting the script.

## How to Run
Run the script from your terminal using the following command:
```bash
python tip_calculator.py
```

## Sample Output
```
================================
      💲 Tip Calculator 💲
================================
Enter the total bill amount: $124.50
Enter the desired tip percentage (e.g., 15, 18, 20): %18
Enter the number of people to split the bill with: 4

--------------------------------
         📋 RESULTS 📋
--------------------------------
  Total Bill:      $124.50
  Tip (18.0%):     +$22.41
  ============================
  Total with Tip:  $146.91

  Each person should pay: $36.73
--------------------------------

Calculate another tip? (y/n): n

Thank you for using the Tip Calculator! 👋
```

## Code Structure
- `tip_calculator.py`: The main Python script.
- `get_numeric_input()`: A reusable function for getting and validating positive numeric input from the user, handling both floats and integers.
- `calculate_and_display()`: The core function that prompts for all inputs, performs the calculations, and prints the formatted results.
- `main()`: The main controller that runs the application loop.

## Enhancements (Optional)
- **Rounding Options**: Ask the user if they want to round the total bill or the per-person amount up to the nearest dollar.
- **Tip Presets**: Offer quick options for common tip percentages (e.g., 1) 15%, 2) 18%, 3) 20%).
- **GUI Version**: Build a graphical user interface for the calculator using a library like Tkinter or PyQt to make it more interactive.
- **Bill Splitting by Item**: A more advanced version could allow users to input individual item costs for a more accurate split.

## Time Estimate
**Beginner**: 45-75 minutes
**With enhancements**: 2-4 hours

## Key Concepts
- Floating-Point Arithmetic
- String Formatting (`.2f`)
- User Input Validation
- Function Reusability
- Type Casting (`float`, `int`)
