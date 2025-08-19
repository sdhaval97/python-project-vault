import random
import os
import time

def clear_screen():
    """Clears the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')
    
def get_game_options():
    """Gets dice type and number from the user with validation."""
    # Get the dice type
    while True:
        dice_type_input = input("Enter the type of dice (d4, d6, d8, d10, d12, d20): ").lower().strip()
        if dice_type_input in ['d4', 'd6', 'd8', 'd10','d12', 'd20']:
            num_sides = int(dice_type_input[1:])
            break
        else:
            print("Invalid input. Please choose from the list.")

    # Get number of dice
    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll (1 or 2): ").strip())
            if num_dice in [1, 2]:
                break
            else:
                print("Invalid input. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
    return num_sides, num_dice

def roll_dice(num_dice, num_sides):
    """
    Simulates rolling dice and returns a list of results.
    Includes a simple text-based animation.
    """
    print("\n...rolling the dice...")
    time.sleep(1) # Pause for effect
    
    results = [random.randint(1, num_sides) for _ in range(num_dice)]
    return results

def display_results(results, num_sides):
    """Displays the ASCII art for d6 dice or text for other types."""
    print("\n"+"="*25)
    print("RESULTS.".center(25))
    print("="*25)
    