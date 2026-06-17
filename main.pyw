#!/usr/bin/env python3
import os
import sys
current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
import funktionen.datum
import tkinter as tk
from tkinter import ttk
sys.path.append(current_dir)
from PIL import Image, ImageTk
from funktionen.center import center_window

class greeting():
    def __init__(self):
        self.root = tk.Tk()
        self.style = ttk.Style()
        self.style.configure("font.TLabel", font=("Arial",15))
        self.style.configure("font.TButton", font=("Arial",15))
        self.image = tk.PhotoImage(file=os.path.join(current_dir, 'GrueneIdylle.png'))
        self.root.iconphoto(True, self.image)
        self.vers_major = str(sys.version_info.major)
        self.vers_minor = str(sys.version_info.minor)
        self.vers_micro = str(sys.version_info.micro)
        self.greet, self.day_of_week, self.day_of_month, self.month, self.year, self.hour, self.minute, self.second = funktionen.datum.datetime()
        self.datetime = f"Heute ist {self.day_of_week}, der {self.day_of_month}. {self.month} {self.year}. Es ist {self.hour:02d}:{self.minute:02d}:{self.second:02d}"
        self.title = f"Es grüsst Python {self.vers_major}.{self.vers_minor}.{self.vers_micro}"
        self.root.title(self.title)
        self.geometry = center_window(805, 750, self.root)
        self.root.geometry(self.geometry)
        self.root.resizable(False, False)
        self.image = Image.open(os.path.join(current_dir, "GrueneIdylle.jpg")).resize((800, 600))
        self.photo = ImageTk.PhotoImage(self.image)
        self.greetings_frame = ttk.Frame(self.root)
        self.greeting_frame = (self.greetings_frame)
        self.greeting = ttk.Label(self.greeting_frame, justify="left", text=self.greet, style="font.TLabel")
        self.greeting.pack(fill="x", padx=5, pady=5)
        self.datetime_frame = ttk.Frame(self.greetings_frame)
        self.datetimelabel = ttk.Label(self.datetime_frame, text=self.datetime, style="font.TLabel")
        self.datetimelabel.pack(side="left", padx=5, pady=5)
        self.datetime_frame.pack(fill="x")
        self.greeting_frame.pack(fill="x")
        self.greetings_frame.pack(fill="x")
        self.photo_label = ttk.Label(self.root, image=self.photo)
        self.photo_label.pack()
        self.destroy_button = ttk.Button(self.root, text="Programm beenden", style="font.TButton", command=self.root.destroy)
        self.destroy_button.pack(side="bottom", pady="10")
        self.root.mainloop()

g = greeting()
