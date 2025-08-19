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
    
    # Use ASCII art only for 1 or 2 6 sided dice
    if num_sides == 6 and len(results) <= 2:
        display_d6_art(results)
    else:
        # for other dice types or 2 or more dice, show numbers
        for i, roll in enumerate(results):
            print(f"- Die #{i+1}: {roll}")
    
    # Print total if more than one die was rolled
    if len(results) > 1:
        print(f"\n Total: {sum(results)}")
    print("="*25)
    
def display_d6_art(results):
    """Display ASCII art for dice"""
    dice_faces = {
        1: ["│    ●    │"], 2: ["│  ●      │", "│      ●  │"],
        3: ["│  ●      │", "│    ●    │", "│      ●  │"],
        4: ["│  ●   ●  │", "│         │", "│  ●   ●  │"],
        5: ["│  ●   ●  │", "│    ●    │", "│  ●   ●  │"],
        6: ["│  ●   ●  │", "│  ●   ●  │", "│  ●   ●  │"]
    }
    
    for i in range(1, 7):
        face = dice_faces[i]
        while len(face) < 3:
            if len(face) == 1: # Center the single dot for 1 and 3
                face.insert(0, "│         │")
                face.append("│         │")
            else: # Add middle blank for 2 and 4
                face.insert(1, "│         │")
                
    # Prepare lines for printing
    lines = [""] * 5
    lines[0] = " ".join(["┌─────────┐"] * len(results))
    lines[4] = " ".join(["└─────────┘"] * len(results))
    
    for i in range(len(results)):
        roll = results[i]
        face = dice_faces[roll]
        lines[1] += f" {face[0]} "
        lines[2] += f" {face[1]} "
        lines[3] += f" {face[2]} "

    for line in lines:
        print(line.strip())

def main():
    """Main application controller."""
    while True:
        clear_screen()
        print("🎲 Welcome to the Advanced Dice Rolling Simulator! 🎲")
        print("=" * 50)
        
        num_sides, num_dice = get_game_options()
        
        results = roll_dice(num_dice, num_sides)
        display_results(results, num_sides)
        
        while True:
            again = input("\nRoll again? (y/n): ").lower().strip()
            if again in ['y', 'yes', 'n', 'no']:
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        
        if again in ['n', 'no']:
            print("\nThanks for playing! 👋")
            break

if __name__ == "__main__":
    main()