#!/usr/bin/env python3

import tkinter as tk
import sys

import algoviz_drawings as viz_dr
import algoviz_sortings as viz_s
from tools import *



def main_frame(window):

    clean_slate(window)

    # Frames for the two sets of buttons
    main_buttons_frame = tk.Frame(window)
    main_buttons_frame.place(relx=0.5, rely=0.3, anchor="center")
    control_buttons_frame = tk.Frame(window, height=50)
    control_buttons_frame.pack(fill ="x", side="bottom")

    # Buttons of the first frame
    sort_button = tk.Button(main_buttons_frame,
                            command= lambda window=window: viz_s.sortings_frame(window),
                            text="Sorting Algorithms")
    sort_button.grid(row=0, column=0, sticky="ew", padx = 10)

    drawings_button = tk.Button(main_buttons_frame,
                                command=lambda window=window: viz_dr.drawings_frame(window),
                                text="Recursive Drawings")
    drawings_button.grid(row=0, column=1, sticky="ew")

    # others_button = tk.Button(main_buttons_frame, text="Others")
    # others_button.grid(row = 1, column = 0, sticky = "ew", padx = 10)

    # enigmas_button = tk.Button(main_buttons_frame, text="Recursive Enigmas")
    # enigmas_button.grid(row = 1, column = 1, sticky="ew")

    # Buttons of the second frame
    docs_button =  tk.Button(control_buttons_frame,
                              command= lambda link="https://github.com/Chuxclub": open_url(link),
                              text="Git Repo")
    docs_button.place(relx= 0.14, y = 20, height=30, width=70)

    exit_button = tk.Button(control_buttons_frame, command= lambda: sys.exit(), text="Exit")
    exit_button.place(relx = 0.48, x = -35, height=50, width = 100)

    author_button = tk.Button(control_buttons_frame,
                              command= lambda
                              link="http://autodilab.hopto.org/Content/Misc/qui_suis_je.html":
                              open_url(link),
                              text="Author")
    author_button.place(relx = 0.78, y = 20, height=30, width=70)

# sierpinski_button = tk.Button(window, command= lambda: sierpinski(1), text="Sierpinski")
# sierpinski_button.place(relx=0.5, rely=0.5, anchor="center")


if __name__ == "__main__":

     window = tk.Tk()
     window.wm_title("Algoviz") # Sets the title of the window
     window.geometry("500x400") # Sets the dimensions of the window

     main_frame(window)
     window.mainloop()