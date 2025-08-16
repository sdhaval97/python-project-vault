import random

def play_game():
    """Main game function that handles a single round of the guessing game"""
    
    # Generate random number between 1 and 100
    secret_number = random.randint(1,100)
    attempts = 0  
    
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Game loop - continues until correct guess is made
    while True:
        guess = get_valid_guess()  # Get validated user input
        attempts += 1  # Increment attempt counter
        
        # Compare guess to secret number and provide feedback
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            # Correct guess - display success message and exit loop
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
            break
            
def get_valid_guess():
    """Get and validate user input for their guess"""
    # Input validation loop - continues until valid input is received
    while True:
        try:
            # Attempt to convert user input to integer
            guess = int(input("Enter your guess (1-100): "))
            # Check if guess is within valid range
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100!")
        except ValueError:
            # Handle non-numeric input
            print("Enter a valid number!")

def play_again():
    """Ask user if they want to play another round and validate their response"""
    # Input validation loop for play again choice
    while True:
        choice = input("\nWould you like to play again? (y/n): ").lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            # Invalid input - prompt user again
            print("Please enter 'y' for yes or 'n' for no.")

def main():
    """Main program entry point - handles game session with multiple rounds"""
    print("=" * 50)
    print("🎮 NUMBER GUESSING GAME")
    print("=" * 50)
    
    # Main game session loop - allows multiple rounds
    while True:
        play_game()  
        # Check if user wants to continue playing
        if not play_again():
            print("\nThanks for playing! 👋")
            break  
            
if __name__ == "__main__":
    main()