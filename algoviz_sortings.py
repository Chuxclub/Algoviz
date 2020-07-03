#!/usr/bin/env python3

import tkinter as tk
import sys

from tools import *
import algoviz as al
from bubble_anim import *


def sortings_frame(window):

    clean_slate(window)

    # Frames for the two sets of buttons
    main_buttons_frame = tk.Frame(window)
    main_buttons_frame.place(relx=0.5, rely=0.3, anchor="center")
    control_buttons_frame = tk.Frame(window, height=50)
    control_buttons_frame.pack(fill ="x", side="bottom")

    # Buttons of the first frame
    bubble_button = tk.Button(main_buttons_frame,
                             command=bubble_anim,
                             text="Bubble Sort")
    bubble_button.grid(row=0, column=0, sticky="ew")



    # Control buttons
    back_button = tk.Button(control_buttons_frame,
                            command= lambda window=window: al.main_frame(window),
                            text="Back")
    back_button.place(relx= 0.14, y = 20, height=30, width=50)

    home_button = tk.Button(control_buttons_frame,
                            command= lambda window=window: al.main_frame(window),
                            text="Home")
    home_button.place(relx = 0.48, x = -35, height=50, width = 100)

    exit_button = tk.Button(control_buttons_frame, command = lambda:sys.exit(), text="Exit")
    exit_button.place(relx = 0.78, y = 20, height=30, width=50)