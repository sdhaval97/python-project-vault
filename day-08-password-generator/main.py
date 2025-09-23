import string
import secrets
import os
import time

def clear_screen():
    """Clears the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')
    
def get_password_specs():
    """Gets password length and character type preferences from the user."""
    clear_screen()
    print("===================================")
    print("  Secure Password Generator")
    print("===================================")
    
    # Get password length
    while True:
        try:
            length_str = input("Enter the desired password length (8-64): ").strip()
            length = int(length_str)
            if 8 <= length <= 64:
                break
            else:
                print("❌ Invalid length. Please enter a number between 8 and 64.")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
            
    include_upper = input("Include uppercase letters? (y/n): ").lower().strip() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower().strip() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower().strip() == 'y'
    
    return length, include_upper, include_numbers, include_symbols

def generate_password(length, use_upper, use_numbers, use_symbols):
    """Generates a password based on the specific criteria"""
    character_pool = list(string.ascii_lowercase)
    password = [secrets.choice(string.ascii_lowercase)]
    
    if use_upper:
        character_pool.extend(string.ascii_uppercase)
        password.append(secrets.choice(string.ascii_lowercase))
    if use_numbers:
        character_pool.extend(string.digits)
        password.append(secrets.choice(string.digits))
    if use_symbols:
        character_pool.extend(string.punctuation)
        password.append(secrets.choice(string.punctuation))
    
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(secrets.choice(character_pool))
    
    secrets.SystemRandom().shuffle(password)
    
    return "".join(password)

def main():
    """Main application controller"""
    while True:
        length, use_upper, use_numbers, use_symbols = get_password_specs()
        
        password = generate_password(length, use_upper, use_numbers, use_symbols)
        print("\n-----------------------------------")
        print("  Generated Password:")
        print(f"  >>> {password} <<<")
        print("-----------------------------------")
        
        again = input("\nGenerate another password? (y/n): ").lower().strip()
        if again != 'y':
            print("\nStay secure! Goodbye! 👋")
            break
        
if __name__ == "__main__":
    main()
                