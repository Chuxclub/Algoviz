#!/usr/bin/env python3

import tkinter as tk
import sys

from tools import *
from algoviz import main_frame
from sierpinski_triangle import *
from binary_trees_anim import *
from broken_lines_anim import *


def drawings_frame(window):

    clean_slate(window)

    # Frames for the two sets of buttons
    main_buttons_frame = tk.Frame(window)
    main_buttons_frame.place(relx=0.5, rely=0.3, anchor="center")
    control_buttons_frame = tk.Frame(window, height=50)
    control_buttons_frame.pack(fill ="x", side="bottom")

    # Buttons of the first frame
    tree_button = tk.Button(main_buttons_frame,
                             command= lambda window=window, drawing_func=draw_btree:
                             drawing_frame(window, drawing_func, 100),
                             text="Trees")
    tree_button.grid(row=0, column=0, sticky="ew")

    blines_button = tk.Button(main_buttons_frame,
                             command= lambda window=window, drawing_func=draw_blines:
                             drawing_frame(window, drawing_func),
                             text="Broken Lines")
    blines_button.grid(row=1, column=0, sticky="ew")

    sierp_button = tk.Button(main_buttons_frame,
                             command= lambda window=window, drawing_func=sierpinski:
                             drawing_frame(window, drawing_func),
                             text="Sierpinski Triangles")
    sierp_button.grid(row = 2, column = 0, sticky = "ew")


    # Control buttons
    back_button = tk.Button(control_buttons_frame,
                            command= lambda window=window: main_frame(window),
                            text="Back")
    back_button.place(relx= 0.14, y = 20, height=30, width=50)

    home_button = tk.Button(control_buttons_frame,
                            command= lambda window=window: main_frame(window),
                            text="Home")
    home_button.place(relx = 0.48, x = -35, height=50, width = 100)

    exit_button = tk.Button(control_buttons_frame, command = lambda:sys.exit(), text="Exit")
    exit_button.place(relx = 0.78, y = 20, height=30, width=50)



class InputEntry():
    def __init__(self, window):
        self.entry_var="1"

        button_frame = tk.Frame(window)
        button_frame.pack(fill="x", padx=10, pady=20)

        iteration_label = tk.Label(button_frame,text="Number of iterations: ")
        self.iteration_entry=tk.Entry(button_frame)

        iteration_label.pack(side="left")
        self.iteration_entry.pack(side="left")
        self.iteration_entry.focus_set()

        update_button= tk.Button(button_frame, text="Update",
                           command=self.update_value).pack(padx=10, side = "left")

    def update_value(self):
        self.entry_var=self.iteration_entry.get()

    def get_value(self):
        return int(self.entry_var)


def launch_drawing(input_entry, animation_func, i, *args):

    i = input_entry.get_value()

    if len(*args) != 0:
        animation_func(i, *args)

    else:
        animation_func(i)


def drawing_frame(window, drawing_func, *args):

    clean_slate(window)

    # Parameters fields
    iteration_field = InputEntry(window)

    generation_frame = tk.Frame(window)
    generation_frame.place(relx = 0.5, rely = 0.3, anchor="center")
    control_buttons_frame = tk.Frame(window, height=50)
    control_buttons_frame.pack(fill ="x", side="bottom")


    # Generation button
    i = iteration_field.get_value()
    gen_button = tk.Button(generation_frame,
                           command = lambda
                           input_entry=iteration_field, i=i,
                           animation_func=drawing_func,
                           others=args:
                           launch_drawing(input_entry, animation_func, i, others),
                           text = "Generate!")
    gen_button.grid()


    # Control buttons
    back_button = tk.Button(control_buttons_frame,
                            command = lambda window=window: drawings_frame(window),
                            text="Back")
    back_button.place(relx= 0.14, y = 20, height=30, width=50)

    home_button = tk.Button(control_buttons_frame,
                            command = lambda window=window: main_frame(window),
                            text="Home")
    home_button.place(relx = 0.48, x = -35, height=50, width = 100)

    exit_button = tk.Button(control_buttons_frame, command = lambda:sys.exit(), text="Exit")
    exit_button.place(relx = 0.78, y = 20, height=30, width=50)