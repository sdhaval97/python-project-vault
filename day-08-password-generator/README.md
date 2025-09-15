# Project 11: Password Generator

## Project Overview
A command-line tool that generates strong, random passwords based on user-specified criteria. This project emphasizes cybersecurity principles by using Python's `secrets` module for cryptographically secure random number generation, which is essential for creating unpredictable and secure passwords.

## What You'll Learn
- **Cryptographically Secure Randomness**: Using the `secrets` module instead of `random` for security-sensitive applications.
- **String Manipulation**: Working with built-in string constants (`string.ascii_letters`, `string.digits`, etc.).
- **Cybersecurity Consciousness**: Understanding the importance of password complexity, entropy, and secure generation practices.
- **Input Validation**: Ensuring user input for password length and criteria is within a safe and valid range.

## Features
- **Customizable Length**: Users can specify a password length between 8 and 64 characters.
- **Character Set Selection**: Users can choose to include uppercase letters, numbers, and symbols.
- **Cryptographically Secure**: Utilizes the `secrets` module to protect against predictability.
- **Guaranteed Complexity**: The generation logic ensures that at least one character from each selected set is included in the final password.
- **User-Friendly Interface**: A simple and clear command-line prompt guides the user through the options.

## How to Run
Run the script from your terminal using the following command:
```bash
python password_generator.py
```

## Sample Output
```
===================================
  Secure Password Generator
===================================
Enter the desired password length (8-64): 16
Include uppercase letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y

-----------------------------------
  Generated Password:
  >>> K&g9!p@wR5v$J3sQ <<<
-----------------------------------

Generate another password? (y/n): n

Stay secure! Goodbye! 👋
```

## Code Structure
- `password_generator.py`: The main Python script.
- `get_password_specs()`: Prompts the user for password length and character type preferences and validates the input.
- `generate_password()`: The core logic for building the character pool and generating the secure password, ensuring all criteria are met.
- `main()`: The main controller that runs the application loop, allowing the user to generate multiple passwords.

## Enhancements (Optional)
- **Copy to Clipboard**: Add a feature to automatically copy the generated password to the clipboard (using a library like `pyperclip`).
- **Password Strength Meter**: Create a function that analyzes the generated password and gives it a strength rating (e.g., weak, medium, strong, very strong).
- **GUI Version**: Build a graphical user interface for the generator using a library like Tkinter or PyQt.
- **Passphrase Generator**: Add an option to generate memorable passphrases by randomly combining words from a wordlist (like the XKCD method).

## Time Estimate
**Beginner**: 60-90 minutes
**With enhancements**: 3-5 hours

## Key Concepts
- `secrets` vs. `random` module
- String Constants
- Boolean Logic
- Input Validation
- List Manipulation and Shuffling
