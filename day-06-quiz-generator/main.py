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
    
    for index, q in enumerate(questions):
        clear_screen()
        print(f"❓ Question {index + 1}/{total_questions}")
        print("="*30)
        print(q["question"])
        print("-" * 30)
        
        for option in q["options"]:
            print(option)
        
        while True:
            user_answer = input("\nEnter your choice (A, B, C, or D): ").upper().strip()
            if user_answer in ['A', 'B', 'C', 'D']:
                break
            else:
                print("Invalid input. Please enter A, B, C, or D.")
        
        correct_answer = q["answer"]
        if user_answer == correct_answer:
            print("\n✅ Correct! Great job.")
            score += 1
        else:
            print(f"\n❌ Incorrect. The correct answer was {correct_answer}.")
        
        time.sleep(2) # Pause for 2 seconds to let the user see the feedback
        
        return score, total_questions
    
    