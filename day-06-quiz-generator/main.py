import json
import os
import time

def clear_screen():
    """Clears the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_questions(filename = 'questions.json'):
    """Loads questions from a json file"""
    try:
        with open(filename, 'r') as file:
            questions = json.load(file)
        return questions
    except FileNotFoundError:
        print(f'Error: The file "{filename}" was not found')
        return None
    except json.JSONDecodeError:
        print(f'Error: The file "{filename}" is not a valid JSON file')
        return None

def run_quiz(questions):
    """Runs the quiz, displays questions, and tracks the score."""
    score = 0
    total_questions = len(questions)
    
    