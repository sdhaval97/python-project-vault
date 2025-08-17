# Day 2: Countdown Timer

## Project Overview
A console-based countdown timer that accepts user input in seconds and counts down to zero with real-time display updates. Perfect for pomodoro sessions, cooking, or any timed activity.

## What You'll Learn
- Using the `time` module
- `time.sleep()` function for delays
- String formatting for time display
- Real-time console updates
- Mathematical time conversions
- Input validation and error handling

## Features
- Input validation for positive numbers
- Real-time countdown display (MM:SS format)
- Visual progress indicators
- Sound/alert when timer reaches zero
- Option to set multiple timers
- Pause/resume functionality (optional)

## How to Run
```bash
python main.py
```

## Sample Output
```
⏰ Countdown Timer

Enter countdown time in seconds: 65

Starting countdown for 01:05

01:04
01:03
01:02
01:01
01:00
00:59
00:58
...
00:03
00:02
00:01
00:00

🚨 TIME'S UP! 🚨
```

## Code Structure
- `main.py` - Main timer application
- Functions for time formatting, countdown logic, and user interface
- Clean separation of concerns with modular functions

## Enhancements (Optional)
- Add hours support (HH:MM:SS format)
- Multiple timer presets (5min, 15min, 30min, 1hr)
- Progress bar visualization
- Sound notification when complete
- Pause/resume with spacebar
- Save/load custom timer presets

## Time Estimate
**Beginner**: 45-75 minutes  
**With enhancements**: 2-3 hours

## Key Concepts
- Time manipulation and formatting
- Console output control
- User input validation
- Loop control and timing
- String formatting techniques