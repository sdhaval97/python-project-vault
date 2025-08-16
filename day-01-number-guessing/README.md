# Day 1: Number Guessing Game

## Project Overview
A classic beginner Python project where the computer generates a random number and the player tries to guess it. The program provides hints ("too high" or "too low") to guide the player toward the correct answer.

## What You'll Learn
- Using the `random` module
- Conditional statements (`if`, `elif`, `else`)
- While loops for game continuation
- User input handling with `input()`
- Basic error handling
- Game logic and flow control

## Features
- Random number generation between 1-100
- Hint system (too high/too low)
- Attempt counter
- Input validation
- Play again functionality
- Difficulty levels (optional enhancement)

## How to Run
```bash
python main.py
```

## Sample Output
```
🎯 Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Enter your guess: 50
Too high! Try again.

Enter your guess: 25
Too low! Try again.

Enter your guess: 37
🎉 Congratulations! You guessed it in 3 attempts!

Would you like to play again? (y/n): n
Thanks for playing!
```

## Code Structure
- `main.py` - Main game file with all functionality
- Functions for game logic, input validation, and replay system
- Clean, readable code with proper comments

## Enhancements (Optional)
- Add difficulty levels (easy: 1-50, medium: 1-100, hard: 1-500)
- Implement a scoring system based on attempts
- Add a high score tracker
- Include ASCII art for celebration
- Add timer functionality

## Time Estimate
**Beginner**: 30-60 minutes  
**With enhancements**: 1-2 hours