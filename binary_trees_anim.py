#!/usr/bin/env python3

import turtle

def draw_btree_aux(pen, stop_index, branch_len):

    if stop_index == 1 :
        pen.backward(branch_len)
        return


    else :

        pos = pen.pos()
        heading = pen.heading()

        pen.left(45)
        pen.forward(branch_len)
        draw_btree_aux(pen, stop_index-1, branch_len*0.7)

        pen.penup()
        pen.goto(pos)
        pen.setheading(heading)
        pen.pendown()

        pen.right(45)
        pen.forward(branch_len)
        draw_btree_aux(pen, stop_index-1, branch_len*0.7)
        

def draw_btree(stop_index, branch_len):

    turtle.TurtleScreen._RUNNING = True # Necessary for Tkinter recall... I don't know why???
    screen = turtle.Screen()
    pen = turtle.Turtle()
    pen.shape("circle")
    pen.shapesize(0.2, 0.2, 0.2)
    # pen.speed(1)
	
    pen.left(90)
    pen.forward(150)
    draw_btree_aux(pen, stop_index, branch_len)

    pen.penup()
    pen.home()

    screen.exitonclick()
    
    turtle.TurtleScreen._RUNNING = True
	
	
	
if __name__ == "__main__":
    draw_btree(6, 100)
