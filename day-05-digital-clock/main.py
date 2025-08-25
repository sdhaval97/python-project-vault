import tkinter as tk
from time import strftime

def create_clock_window():
    """Creates the main window for the digital clock"""
    window = tk.Tk()
    window.title("Digital Clock")
    window.geometry("420x150")
    window.resizable(False, False)
    window.configure(bg="black")
    return window

def create_clock_label(window):
    """Creates the label that will display the time"""
    clock_label = tk.Label(
        window,
        font=('calibri', 60, 'bold'),
        background='black',
        foreground='cyan'
    )
    clock_label.pack(anchor='center', pady=30)
    return clock_label

def update_time(clock_label):
    """
    Gets the current time and updates the clock label.
    This function calls itself every 1s to keep the time updated.
    """
    # Get current time in Hour:Minute:Second format
    current_time = strftime('%H:%M:%S %p')
    
    # Update the label's text with the current time
    clock_label.config(text=current_time)
    
    # Schedule the update_time function to be called after 1s
    clock_label.after(1000, lambda:update_time(clock_label))

def main():
    """To set up and run the clock app"""
    # I. Create the main application window
    app_window = create_clock_window()
    
    # II. Create the label widget to display the time
    time_label = create_clock_label(app_window)
    
    # III. Start the time-updating process
    update_time(time_label)
    
    # IV. Start the Tkinter event loop
    app_window.mainloop()

if __name__ == "__main__":
    main()