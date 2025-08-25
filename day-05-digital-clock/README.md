# Project 8: A Digital Clock in Tkinter

## Project Overview
A graphical user interface (GUI) application that displays the current time in a digital format. Built with Python's standard Tkinter library, this project serves as an excellent introduction to GUI development and event-driven programming, creating a real-time, updating timepiece on your desktop.

## What You'll Learn
- **GUI Fundamentals**: How to create and configure a basic window using Tkinter.
- **Tkinter Widgets**: Using the `Label` widget to display dynamic text.
- **Event-Driven Programming**: Understanding how to schedule a function to run repeatedly using the `.after()` method to create a real-time clock.
- **Layout Management**: Using the `.pack()` manager to position widgets within the window.
- **Aesthetics and Styling**: Customizing the appearance of a GUI, including fonts, colors, and window size.

## Features
- **Real-Time Updates**: The clock face updates every second without freezing the application.
- **Clean Digital Display**: Shows the current time in a clear `HH:MM:SS` format.
- **Customizable Appearance**: The clock has a sleek black background with a cyan digital-style font.
- **Simple and Lightweight**: Built entirely with Python's standard library, requiring no external dependencies.

## How to Run
```bash
python digital_clock.py
```

## Sample Output
When you run the script, a new window will appear on your screen displaying the current time, which updates every second.

!

## Code Structure
- `digital_clock.py` - The main application file.
- `create_clock_window()`: A function dedicated to setting up the main application window and its properties (title, size, color).
- `create_clock_label()`: A function that creates and styles the `Label` widget where the time is displayed.
- `update_time()`: The core function of the application. It fetches the current time and uses `strftime` to format it, then schedules itself to run again after one second.
- `main()`: The main controller that orchestrates the creation of the UI and starts the Tkinter event loop.

## Enhancements (Optional)
- **Add the Date**: Modify the display to include the current date (e.g., "YYYY-MM-DD").
- **Timezone Selector**: Add a dropdown menu to select and display the time in different timezones.
- **Alarm Clock**: Implement functionality to set an alarm that triggers a sound or a message box at a specific time.
- **Customization Options**: Add menus to allow the user to change the font color, background color, or time format (12-hour vs. 24-hour).

## Time Estimate
**Beginner**: 45-75 minutes
**With enhancements**: 3-5 hours

## Key Concepts
- GUI Programming (Tkinter)
- Event-Driven Architecture
- The `time` module and `strftime()`
- Widget Styling and Layout
- Recursive Function Scheduling (`.after()`)
