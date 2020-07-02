#!/usr/bin/env python3

import turtle
import numpy as np

screen = turtle.Screen()
pen = turtle.Turtle()
# pen.pencolor("red")
pen.fillcolor("red")
# pen.speed(1)


# =======================================================================

def draw_heart(radius, spine_len):

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # ~~~~~~~~~~ STARTING HEART SHAPE DRAWING WITH RED FILLING ~~~~~~~~ #
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    pen.begin_fill()

    # Drawing left cheek
    pen.seth(90)
    pen.circle(radius, extent=210)
    pos_left = pen.pos()

    # Getting back to the origin, facing north
    pen.up()
    pen.home()
    pen.seth(90)

    # Drawing right cheek
    pen.down()
    pen.circle(-radius, extent=210)
    pos_right = pen.pos()

    # Getting back to the origin, facing south...
    # Then going right to the bottom of the heart shape
    pen.up()
    pen.home()
    pen.seth(270)
    pen.forward(spine_len)
    bottom = pen.pos()

    # Drawing the left and right edges
    pen.down()
    pen.setpos(pos_left)
    pen.up()
    pen.setpos(bottom)
    pen.down()
    pen.setpos(pos_right)

    pen.end_fill()

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

    # Repairing unfilled part of the heart
    pen.up()
    pen.home()
    pen.begin_fill()
    pen.seth(270)
    pen.forward(spine_len)
    pen.setpos(pos_left)
    pen.home()
    pen.end_fill()

# ========================================================================

def main():
    pen.hideturtle()
    draw_heart(50, 150)
    turtle.mainloop() # To maintain the window open (why doesn't it do it by default?)

main()