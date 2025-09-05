# Project 7: The Terminal To-Do List

## Project Overview
A minimalist but functional command-line to-do list application. This tool allows users to add, view, and delete tasks. All tasks are saved to a local text file, ensuring that the to-do list persists across different sessions.

## What You'll Learn
- **File Handling**: The core of the project. You'll learn how to read from (`r`) and write to (`w`) text files to achieve data persistence.
- **List Operations**: Manipulating lists to add (`append`), remove (`pop`), and display items.
- **Input Parsing and Validation**: Handling user input from the command line, including converting strings to integers and checking for valid choices.
- **Application State**: Understanding how to load the application's state from a file at the start and save it before exiting.

## Features
- **Persistent Storage**: Tasks are saved in a `tasks.txt` file and are reloaded every time the app starts.
- **Add Tasks**: Easily append new tasks to your list.
- **View Tasks**: Display a clean, numbered list of all your current tasks.
- **Delete Tasks**: Remove tasks by their number from the list.
- **Minimalist Interface**: A clean, straightforward command-line interface that is easy to navigate.

## How to Run
1.  Save the code as `todo_app.py`.
2.  Run it from your terminal:
```bash
python todo_app.py
```
A `tasks.txt` file will be automatically created in the same directory to store your tasks.

## Sample Output
```
==========================
  Terminal To-Do List
==========================
  1. View Tasks
  2. Add Task
  3. Delete Task
  4. Exit
--------------------------
Choose an option (1-4): 2

--- Add a New Task ---
Enter the task description: Finish the README file

✅ Task 'Finish the README file' added!

[Screen clears]

==========================
  Terminal To-Do List
==========================
...
Choose an option (1-4): 1

~~~~~~~~~~~~~~~~~~~~~~~~~~
📝      YOUR TASKS      📝
~~~~~~~~~~~~~~~~~~~~~~~~~~
  1. Buy groceries
  2. Finish the README file

~~~~~~~~~~~~~~~~~~~~~~~~~~

Press Enter to return to the menu...
```

## Code Structure
- `tasks.txt`: The text file used for persistent storage.
- `todo_app.py`: The main application script.
- `load_tasks()`: Reads all lines from `tasks.txt` into a list when the application starts.
- `save_tasks()`: Writes the current list of tasks back into `tasks.txt`.
- `view_tasks()`, `add_task()`, `delete_task()`: Functions that handle the core logic for each user action.
- `main()`: The main controller that runs the application loop and presents the user menu.

## Enhancements (Optional)
- **Mark as Complete**: Instead of just deleting, add an option to mark tasks as "done" (e.g., by adding an `[x]` prefix).
- **Timestamps**: Automatically add a timestamp when a task is created.
- **Prioritization**: Allow users to assign a priority level (e.g., High, Medium, Low) to each task and sort the list by priority.
- **Edit Tasks**: Add functionality to edit an existing task.

## Time Estimate
**Beginner**: 60-90 minutes
**With enhancements**: 3-4 hours

## Key Concepts
- File I/O (Input/Output)
- List Indexing and Manipulation
- Persistent State
- Command-Line Interfaces (CLI)
- Modular Functions
