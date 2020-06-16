#!/usr/bin/env python3

import turtle

screen = turtle.Screen()
pen = turtle.Turtle()
# pen.speed(1)

def draw_btree(stop_index, branch_len):

    if stop_index == 1 :
        pen.backward(branch_len)
        return


    else :

        pos = pen.pos()
        heading = pen.heading()

        pen.left(45)
        pen.forward(branch_len)
        draw_btree(stop_index-1, branch_len*0.7)

        pen.penup()
        pen.goto(pos)
        pen.setheading(heading)
        pen.pendown()

        pen.right(45)
        pen.forward(branch_len)
        draw_btree(stop_index-1, branch_len*0.7)

pen.left(90)
pen.forward(150)
draw_btree(6, 100)

pen.penup()
pen.home()

turtle.mainloop() # To maintain the window open (why doesn't it do it by default?)