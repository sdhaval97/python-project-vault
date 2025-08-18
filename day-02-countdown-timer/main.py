import time
import os 
import sys

def format_time(seconds):
    """Convert seconds to MM:SS or HH:MM:SS format"""
    if seconds >= 3600:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        remaining_seconds = seconds % 60
        return f"{hours:02d}:{minutes:02d}:{remaining_seconds:02d}"
    else:
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        return f"{minutes:02d}:{remaining_seconds:02d}"

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def update_display(time_left, total_time):
    """Update the countdown display"""
    clear_screen()
    
    print("⏰ COUNTDOWN TIMER")
    print("="*40)
    print(f"Time Remaining: {format_time(time_left)}")
    
    # Progress bar
    if total_time > 0:
        progress = (total_time - time_left)/total_time
        bar_length = 30
        filled = int(bar_length * progress)
        bar = "█" * filled + "░" * (bar_length - filled)
        print(f"Progress: [{bar}] {progress:.1%}")
    
    print("=" * 40)
    print("Press Ctrl+C to stop")

def timer_finished():
    """Handle timer completion"""
    clear_screen()
    
    print("🚨" * 20)
    print("🚨" + " " * 16 + "TIME'S UP!" + " " * 16 + "🚨")
    print("🚨" * 20)
    
    # Flash effect with beeps
    for _ in range(5):
        time.sleep(0.3)
        print("\a", end="", flush=True)
        time.sleep(0.3)

def get_timer_duration():
    """Get valid timer duration from user"""
    while True:
        try:
            duration = input("\nEnter countdown time in seconds: ")
            seconds = int(duration)
            
            if seconds <= 0:
                print("Please enter a positive number!")
                continue
            elif seconds > 86400: # 24 hours
                print("Maximum timer duration is 24 hours (86400 seconds)")
                continue
            else:
                return seconds
        except ValueError:
            print("Please enter a valid number!")

def show_presets():
    """Display common timer presets"""
    presets = {
        '1': (300, "5 minutes (Pomodoro break)"),
        '2': (900, "15 minutes (Short break)"),
        '3': (1500, "25 minutes (Pomodoro session)"),
        '4': (1800, "30 minutes (Focus session)"),
        '5': (3600, "1 hour (Deep work)"),
        '6': (0, "Custom time")
    }
    
    print("\n⏰ Timer Presets:")
    print("-" * 40)
    for key, (seconds, description) in presets.items():
        print(f"{key}. {description}")
    
    while True:
        choice = input("\nSelect preset (1-6): ").strip()
        if choice in presets:
            seconds, description = presets[choice]
            if seconds == 0:
                return get_timer_duration()
            else:
                print(f"Selected: {description}")
                return seconds
        else:
            print("Please enter a number between 1-6")
            
def countdown_timer(duration):
    """Main countdown logic"""
    total_time = duration
    
    print(f"\nStarting countdown for {format_time(duration)}")
    input("Press Enter to Start...")
    
    try:
        for remaining in range(duration, -1, -1):
            update_display(remaining, total_time)
            
            if remaining == 0:
                break
            
            time.sleep(1)
            
        # Timer finished
        timer_finished()
    except KeyboardInterrupt:
        print("\n\n⏹️  Timer stopped by user")
        return False
    
    return True

        
                
        
        