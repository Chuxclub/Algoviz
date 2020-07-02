#!/usr/bin/env python3

import tkinter as tk
import sys
from sierpinski_triangle import *
from binary_trees_anim import *
from broken_lines_anim import *

window = tk.Tk()
window.wm_title("Algoviz") # Sets the title of the window
window.geometry("500x400") # Sets the dimensions of the window


def clean_slate(window_name):

     for widget in window_name.winfo_children():
        widget.destroy()


def drawings_frame():

    clean_slate(window)

    # Frames for the two sets of buttons
    main_buttons_frame = tk.Frame(window)
    main_buttons_frame.place(relx=0.5, rely=0.3, anchor="center")
    control_buttons_frame = tk.Frame(window, height=50)
    control_buttons_frame.pack(fill ="x", side="bottom")

    # Buttons of the first frame
    tree_button = tk.Button(main_buttons_frame, command= lambda:draw_btree(6, 100), text="Trees")
    tree_button.grid(row=0, column=0, sticky="ew")

    blines_button = tk.Button(main_buttons_frame, command= lambda:draw_blines(4),
                              text="Broken Lines")
    blines_button.grid(row=1, column=0, sticky="ew")

    sierp_button = tk.Button(main_buttons_frame, command= lambda:sierpinski(3),
                             text="Sierpinski Triangles")
    sierp_button.grid(row = 2, column = 0, sticky = "ew")


    # Buttons of the second frame
    back_button = tk.Button(control_buttons_frame, command=main_frame, text="Back")
    back_button.place(relx= 0.14, y = 20, height=30, width=50)

    home_button = tk.Button(control_buttons_frame, command=main_frame, text="Home")
    home_button.place(relx = 0.48, x = -35, height=50, width = 100)

    exit_button = tk.Button(control_buttons_frame, command = lambda:sys.exit(), text="Exit")
    exit_button.place(relx = 0.78, y = 20, height=30, width=50)


def main_frame():

    clean_slate(window)

    # Frames for the two sets of buttons
    main_buttons_frame = tk.Frame(window)
    main_buttons_frame.place(relx=0.5, rely=0.3, anchor="center")
    control_buttons_frame = tk.Frame(window, height=50)
    control_buttons_frame.pack(fill ="x", side="bottom")

    # Buttons of the first frame
    sort_button = tk.Button(main_buttons_frame, text="Sorting Algorithms")
    sort_button.grid(row=0, column=0, sticky="ew", padx = 10)

    drawings_button = tk.Button(main_buttons_frame,
                                command=drawings_frame,
                                text="Recursive Drawings")
    drawings_button.grid(row=0, column=1, sticky="ew")

    others_button = tk.Button(main_buttons_frame, text="Others")
    others_button.grid(row = 1, column = 0, sticky = "ew", padx = 10)

    enigmas_button = tk.Button(main_buttons_frame, text="Recursive Enigmas")
    enigmas_button.grid(row = 1, column = 1, sticky="ew")

    # Buttons of the second frame
    docs_button = tk.Button(control_buttons_frame, text="Docs")
    docs_button.place(relx= 0.14, y = 20, height=30, width=50)

    exit_button = tk.Button(control_buttons_frame, command= lambda: sys.exit(), text="Exit")
    exit_button.place(relx = 0.48, x = -35, height=50, width = 100)

    author_button = tk.Button(control_buttons_frame, text="Author")
    author_button.place(relx = 0.78, y = 20, height=30, width=50)

# sierpinski_button = tk.Button(window, command= lambda: sierpinski(1), text="Sierpinski")
# sierpinski_button.place(relx=0.5, rely=0.5, anchor="center")


if __name__ == "__main__":
    main_frame()
    window.mainloop()