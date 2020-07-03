#!/usr/bin/env python3
import webbrowser

def clean_slate(window_name):

     for widget in window_name.winfo_children():
        widget.destroy()

def open_url(link):
     webbrowser.open(link, new=2)