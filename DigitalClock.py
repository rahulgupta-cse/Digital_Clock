#Initial setup of Tkinter digital clock project
import tkinter as tk
from time import strftime
from datetime import datetime
from tkinter import messagebox

#Create main application window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x300")

#Default Settings
is_24_hour = True
dark_mode = True
alarm_time = ""

#funtion for update the clock
def time():
    global is_24_hour

    #Time Format(12hr / 24hr)
    if is_24_hour:
        clock = strftime("%H:%M:%S \n %D")
    else:
        clock = strftime("%H:%M:%S %p \n %D")
    
    label.config(text=clock)

    #Alarm checking logic 
    current_time = datetime.now().strftime("%H:%M")
    if alarm_time == current_time:
        messagebox.showinfo("Alarm", "Time's up!")
    label.after(1000,time)

#Toggle time format
def toggle_format():
    global is_24_hour
    is_24_hour = not is_24_hour

#Toggle dark/light mode
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode

    if dark_mode:
        root.config(bg="#272757")
        label.config(bg="#272757",fg="#F2D3F4")
    else:
        root.config(bg="white")
        label.config(bg="white",fg="black")

#Set Alarm function
def set_alarm():
    global alarm_time
    alarm_time = alarm_time.get()
    messagebox.showinfo("Alarm Set",f"Alarm set for {alarm_time}")

#Clock label UI
label = tk.Label(
    root,
    font=('calibri', 40),
    background="#272757",
    foreground="#E2D3F4"
)
label.pack(pady=20)

#Buttons for features
frame = tk.Frame(root)
frame.pack()

# Buttons to change Time Format 
format_btn = tk.Button(frame, text="Toggle 12/24 Hr", command=toggle_format)
format_btn.grid(row=0, column=0, padx=10)

theme_btn = tk.Button(frame, text="Toggle Theme", command=toggle_theme)
theme_btn.grid(row=0, column=1, padx=10)

#Alarm input UI
alarm_entry = tk.Entry(root)
alarm_entry.pack(pady=10)
alarm_entry.insert(0, "HH:MM")

alarm_btn = tk.Button(root, text="Set Alarm", command=set_alarm)
alarm_btn.pack()

#Start clock
time()

# Run application
root.mainloop()