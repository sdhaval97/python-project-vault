import random

def play_game():
    
    # Generate random number between 1 and 100
    secret_number = random.randint(1,100)
    attempts = 0
    
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        try:
            # Get user input
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            # check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                break
    
        except ValueError:
            print("Please enter a valid number!")
     