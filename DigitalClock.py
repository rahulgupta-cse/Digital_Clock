#Initial setup of Tkinter digital clock project
# import tkinter as tk
# Commit 1: Initial setup of Tkinter digital clock project
import tkinter as tk
from time import strftime
from datetime import datetime
from tkinter import messagebox

# Commit 2: Create main application window
root = tk.Tk()
root.title("Advanced Digital Clock")
root.geometry("500x300")

# Commit 3: Default settings
is_24_hour = True
dark_mode = True
alarm_time = ""

# Commit 4: Function to update clock
def funtime():
    global is_24_hour
    
    # Commit 5: Time format toggle (12hr / 24hr)
    if is_24_hour:
        clock = strftime("%H:%M:%S \n %D")
    else:
        clock = strftime("%I:%M:%S %p \n %D")
    
    label.config(text=clock)
    
    # Commit 6: Alarm checking logic
    current_time = datetime.now().strftime("%H:%M")
    if alarm_time == current_time:
        messagebox.showinfo("Alarm", "⏰ Time's up!")
    
    label.after(1000, funtime)

# Commit 7: Toggle time format
def toggle_format():
    global is_24_hour
    is_24_hour = not is_24_hour

# Commit 8: Toggle dark/light mode
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    
    if dark_mode:
        root.config(bg="#272757")
        label.config(bg="#272757", fg="#E2D3F4")
    else:
        root.config(bg="white")
        label.config(bg="white", fg="black")

# Commit 9: Set alarm function
def set_alarm():
    global alarm_time
    alarm_time = alarm_entry.get()
    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time}")

# Commit 10: Clock label UI
label = tk.Label(
    root,
    font=('calibri', 40),
    background="#272757",
    foreground="#E2D3F4"
)
label.pack(pady=20)

# Commit 11: Buttons for features
frame = tk.Frame(root)
frame.pack()

format_btn = tk.Button(frame, text="Toggle 12/24 Hr", command=toggle_format)
format_btn.grid(row=0, column=0, padx=10)

theme_btn = tk.Button(frame, text="Toggle Theme", command=toggle_theme)
theme_btn.grid(row=0, column=1, padx=10)

# Commit 12: Alarm input UI
alarm_entry = tk.Entry(root)
alarm_entry.pack(pady=10)
alarm_entry.insert(0, "HH:MM")

alarm_btn = tk.Button(root, text="Set Alarm", command=set_alarm)
alarm_btn.pack()

# Commit 13: Start clock
funtime()

# Commit 14: Run application
root.mainloop()

# Commit 15: Final version ready for GitHub portfolio 🚀