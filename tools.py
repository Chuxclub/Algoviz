#!/usr/bin/env python3


def clean_slate(window_name):

     for widget in window_name.winfo_children():
        widget.destroy()