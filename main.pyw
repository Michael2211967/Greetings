#!/usr/bin/env python3

import sys
import datum
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class greeting():
    def __init__(self):
        self.root = tk.Tk()
        self.vers_major = str(sys.version_info.major)
        self.vers_minor = str(sys.version_info.minor)
        self.vers_micro = str(sys.version_info.micro)
        self.date = datum.datetime()
        self.begr = f"{self.date[0]}, {self.date[1]}"
        self.datetime = f"Heute ist {self.date[2]}, der {self.date[3]}. {self.date[4]} {self.date[5]}. Es ist {self.date[6]:02d}:{self.date[7]:02d}:{self.date[8]:02d}"
        self.title = "Es grüsst Python " + self.vers_major + "." + self.vers_minor + "." + self.vers_micro
        self.root.title(self.title)
        self.root.geometry("805x683")
        self.root.resizable(False, False)
        self.image = Image.open("GrueneIdylle.jpg").resize((800, 600))
        self.photo = ImageTk.PhotoImage(self.image)
        self.greetings_frame = ttk.Frame(self.root)
        self.greeting_frame = (self.greetings_frame)
        self.greeting = ttk.Label(self.greeting_frame, justify="left", text=self.begr, font="Arial 15")
        self.greeting.pack(fill="x")
        self.datetime_frame = ttk.Frame(self.greetings_frame)
        self.datetimelabel = ttk.Label(self.datetime_frame, text=self.datetime, font="Arial 15")
        self.datetimelabel.pack(side="left")
        self.datetime_frame.pack(fill="x")
        self.greeting_frame.pack(fill="x")
        self.greetings_frame.pack(fill="x")
        self.photo_label = ttk.Label(self.root, image=self.photo)
        self.photo_label.pack()
        self.destroy_button = ttk.Button(self.root, text="Programm beenden", command=self.root.destroy)
        self.destroy_button.pack(side="bottom")
        self.root.mainloop()

g = greeting()
