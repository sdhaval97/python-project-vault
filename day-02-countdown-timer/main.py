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
    
        