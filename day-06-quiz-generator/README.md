# Project 6: Quiz App

## Project Overview
A command-line quiz application that tests a user's knowledge with multiple-choice questions. The app loads questions and answers from an external JSON file, making it easy to customize and expand. It provides immediate feedback after each question and displays a final score upon completion.

## What You'll Learn
- **Working with External Data**: Reading and parsing data from a JSON file.
- **Data Structures**: Using lists and dictionaries to manage the quiz content (questions, options, answers).
- **Data Integrity**: Understanding the importance of separating data (the questions) from logic (the application code).
- **Flow Control**: Managing the application flow with loops and conditional statements.
- **Input Validation**: Ensuring user input is valid before processing.

## Features
- **External Question Source**: Questions are loaded from a `questions.json` file, allowing for easy updates without changing the code.
- **Multiple-Choice Format**: Supports classic A, B, C, D multiple-choice questions.
- **Instant Feedback**: The app tells the user if their answer was correct or incorrect immediately.
- **Score Tracking**: Keeps track of the user's score throughout the quiz.
- **Final Score Summary**: Displays the total score and percentage at the end of the quiz.

## How to Run
1.  Make sure you have both `quiz_app.py` and `questions.json` in the same directory.
2.  Open your terminal and navigate to that directory.
3.  Run the application with the following command:

```bash
python quiz_app.py
```

## Sample Output
```
❓ Question 1/5
==============================
What is the capital of France?
------------------------------
A. London
B. Berlin
C. Paris
D. Madrid

Enter your choice (A, B, C, or D): C

✅ Correct! Great job.

[Screen clears after 2 seconds]

🎉 Quiz Complete! 🎉
==============================
Your final score is: 4/5
You answered 80.00% of the questions correctly.

👍 Excellent work!
```

## Code Structure
- `questions.json`: A file containing the quiz data as a list of JSON objects.
- `quiz_app.py`: The main Python script.
- `load_questions()`: Handles opening and parsing the JSON file, with error handling for missing or invalid files.
- `run_quiz()`: The core function that iterates through questions, gets user input, checks answers, and updates the score.
- `display_final_score()`: A function to show the final results and a congratulatory message.
- `main()`: The main controller that initializes and runs the quiz.

## Enhancements (Optional)
- **Topic Selection**: Store questions for different topics in separate JSON files and let the user choose a topic.
- **Difficulty Levels**: Add a "difficulty" key to each question object and allow the user to select a difficulty level.
- **Timed Quiz**: Add a timer for each question or for the entire quiz.
- **High Score Board**: Save the user's name and score to a file to create a persistent high score list.

## Time Estimate
**Beginner**: 75-120 minutes
**With enhancements**: 4-6 hours

## Key Concepts
- JSON Data Handling
- File I/O (`open()`, `with`)
- Lists and Dictionaries
- Error Handling (`try`/`except`)
- String Formatting
