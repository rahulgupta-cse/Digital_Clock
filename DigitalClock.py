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