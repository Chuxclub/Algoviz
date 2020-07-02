#!/usr/bin/env python3

import turtle
import numpy as np


# pen.speed(1)

# Angle is 60 degree:
def draw_blines_aux(pen, stop_index, branch_len):

    if stop_index == 0:
        pen.forward(branch_len)

    else:
        pen.forward(branch_len/3)

        # Cf. Trigonometry...
        line_len = (branch_len / 3)

        pen.left(60)
        draw_blines_aux(pen, stop_index-1, line_len)
        pen.right(120)
        draw_blines_aux(pen, stop_index-1, line_len)
        pen.left(60)

        pen.forward(branch_len/3)


def draw_blines(stop_index):

    turtle.TurtleScreen._RUNNING = True # Necessary for Tkinter recall... I don't know why???
    screen = turtle.Screen()
    screen_width = screen.window_width()
    pen = turtle.Turtle()
    pen.shape("circle")
    pen.shapesize(0.2, 0.2, 0.2)
    new_home = (-(screen_width/2), 0)
    
    # Setting pen on the left border edge
    pen.penup()
    pen.setpos(new_home)
    pen.pendown()
    
    draw_blines_aux(pen, stop_index, screen_width)
    
    pen.penup()
    pen.setpos(new_home)
    
    screen.exitonclick()



if __name__ == "__main__":
    draw_blines(5)




# Angle is 45 degree:
#
# def draw_blines_aux(stop_index, branch_len):

#     if stop_index == 0:
#         pen.forward(branch_len)

#     else:
#         pen.forward(branch_len/3)

#         # Cf. Trigonometry...
#         line_len = (branch_len / 6) / (np.sqrt(2) / 2)

#         pen.left(45)
#         draw_blines_aux(stop_index-1, line_len)
#         pen.right(90)
#         draw_blines_aux(stop_index-1, line_len)
#         pen.left(45)

#         pen.forward(branch_len/3)


# def draw_blines(stop_index):
#     global screen_width
#     draw_blines_aux(stop_index, screen_width)
