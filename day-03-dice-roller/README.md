# Project 3: Advanced Dice Rolling Simulator

## Project Overview
An interactive console application that simulates rolling various types of polyhedral dice used in tabletop games. Users can select from different dice types (d4, d6, d8, d10, d12, d20) and choose to roll one or two at a time. The simulator displays results clearly, using ASCII art for standard d6 rolls.

## What You'll Learn
- Advanced user input validation for specific choices.
- Conditional logic to change program behavior based on user input.
- Handling different data types and displaying them appropriately.
- Expanding a simple tool into a more flexible and powerful one.
- Writing modular functions that handle specific parts of the program (options, rolling, displaying).

## Features
- **Multiple Dice Types**: Supports d4, d6, d8, d10, d12, and d20 dice.
- **Selectable Dice Count**: User can choose to roll either one or two dice.
- **Conditional ASCII Art**: Displays a visual representation for 1 or 2 d6 rolls.
- **Clear Text Output**: Shows numerical results for all other dice types.
- **Calculated Total**: Automatically calculates and displays the sum when rolling two dice.
- **Robust Input Handling**: Ensures the user selects valid options before proceeding.
- **Play Again Loop**: Allows for continuous rolling without restarting the script.

## How to Run
```bash
python dice_roller.py
```

## Sample Output
```
🎲 Welcome to the Advanced Dice Rolling Simulator! 🎲
==================================================
Enter the type of dice (d4, d6, d8, d10, d12, d20): d20
Enter the number of dice to roll (1 or 2): 2

...rolling the dice...

=========================
         RESULTS
=========================
  - Die #1: 17
  - Die #2: 5

  Total: 22
=========================

Roll again? (y/n): y
```

## Code Structure
- `dice_roller.py` - The main application file.
- `get_game_options()`: Prompts the user for dice type and count with validation.
- `roll_dice()`: Generates random numbers based on the user's choices.
- `display_results()`: The main display function that decides whether to show ASCII art or text.
- `display_d6_art()`: A specialized function to draw the ASCII art for d6 dice.
- `main()`: The main controller function that runs the game loop.

## Enhancements (Optional)
- **Roll More Dice**: Allow the user to roll any number of dice (e.g., "3d8").
- **Modifiers**: Let the user add a modifier to their roll (e.g., "d20 + 5").
- **History**: Keep a log of the previous rolls and display it.
- **Advantage/Disadvantage**: Implement the D&D 5e mechanic of rolling two d20s and taking the higher or lower result.

## Time Estimate
**Beginner**: 75-120 minutes
**With enhancements**: 3-5 hours

## Key Concepts
- Conditional Logic
- User Input Validation
- Data Structures (Lists & Dictionaries)
- Function Decomposition
- String Manipulation
