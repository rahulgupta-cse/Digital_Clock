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

#tToggle time format
def toggle_format():
    global is_24_hour
    is_24_hour = not is_24_hour