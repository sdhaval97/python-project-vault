import random

def play_game():
    
    # Generate random number between 1 and 100
    secret_number = random.randint(1,100)
    attempts = 0
    
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        guess = get_valid_guess()
        attempts += 1
        
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
            break
            
def get_valid_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100!")
        except ValueError:
            print("Enter a valid number!")

def play_again():
    while True:
        choice = input("\nWould you like to play again? (y/n): ").lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def main():
    print("=" * 50)
    print("🎮 NUMBER GUESSING GAME")
    print("=" * 50)
    
    while True:
        play_game()
        if not play_again():
            print("\nThanks for playing! 👋")
            break
            
if __name__ == "__main__":
    main()