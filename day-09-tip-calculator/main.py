import os
import time

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
def get_numeric_input(prompt, input_type=float):
    """Generic function to get and validate numeric input."""
    while True:
        try:
            value_str = input(prompt).strip()
            value = input_type(value_str)
            if value > 0:
                return value
            else:
                print("❌ Please enter a positive number greater than zero.")
        except ValueError:
            print(f"❌ Invalid input. Please enter a valid {'number' if input_type is float else 'integer'}.")

def calculate_and_display():
    """Gets inputs, calculates the tip, and displays the results."""
    clear_screen()
    print("================================")
    print("      💲 Tip Calculator 💲")
    print("================================")

    # Get user inputs
    bill_amount = get_numeric_input("Enter the total bill amount: $")
    tip_percentage = get_numeric_input("Enter the desired tip percentage (e.g., 15, 18, 20): %")
    num_people = get_numeric_input("Enter the number of people to split the bill with: ", int)
    
    # Calculate amounts
    tip_amount = bill_amount * (tip_percentage / 100)
    total_bill = bill_amount + tip_amount
    amount_per_person = total_bill / num_people
    
    # Display results
    print("\n--------------------------------")
    print("         📋 RESULTS 📋")
    print("--------------------------------")
    print(f"  Total Bill:      ${bill_amount:.2f}")
    print(f"  Tip ({tip_percentage}%):  +${tip_amount:.2f}")
    print("  ============================")
    print(f"  Total with Tip:  ${total_bill:.2f}")
    print(f"\n  Each person should pay: ${amount_per_person:.2f}")
    print("--------------------------------")
    
def main():
    """Main application controller"""
    while True:
        calculate_and_display()
        
        again = input("\nCalculate another tip? (y/n): ").lower().strip()
        if again != 'y':
            print("\nThank you for using the Tip Calculator! 👋")
            break

if __name__ == "__main__":
    main()