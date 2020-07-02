#!/usr/bin/env python3

import turtle

def draw_triangle(pen, triangle):

    pen.up()
    pen.setpos(triangle[0])
    pen.down()

    pen.setpos(triangle[1])
    pen.setpos(triangle[2])
    pen.setpos(triangle[0])

    pen.up()


def sierpinski_aux(pen, stop_index, outer_triangle, inner_triangle):

    if stop_index == 0 :
        return

    else:

        draw_triangle(pen, inner_triangle)

        outer_triangle1 = [outer_triangle[0], inner_triangle[0], inner_triangle[2]]
        corner11 = ((outer_triangle[0][0] + inner_triangle[0][0]) / 2,
                    (outer_triangle[0][1] + inner_triangle[0][1]) / 2)
        corner12 =  ((inner_triangle[0][0] + inner_triangle[2][0]) / 2,
                    (inner_triangle[0][1] + inner_triangle[2][1]) / 2)
        corner13 =  ((outer_triangle[0][0] + inner_triangle[2][0]) / 2,
                    (outer_triangle[0][1] + inner_triangle[2][1]) / 2)
        inner_triangle1 = [corner11, corner12, corner13]
        sierpinski_aux(pen, stop_index-1, outer_triangle1, inner_triangle1)

        outer_triangle2 = [inner_triangle[0], outer_triangle[1], inner_triangle[1]]
        corner21 =  ((inner_triangle[0][0] + outer_triangle[1][0]) / 2,
                    (inner_triangle[0][1] + outer_triangle[1][1]) / 2)
        corner22 =  ((outer_triangle[1][0] + inner_triangle[1][0]) / 2,
                    (outer_triangle[1][1] + inner_triangle[1][1]) / 2)
        corner23 =  ((inner_triangle[1][0] + inner_triangle[0][0]) / 2,
                    (inner_triangle[1][1] + inner_triangle[0][1]) / 2)
        inner_triangle2 = [corner21, corner22, corner23]
        sierpinski_aux(pen, stop_index-1, outer_triangle2, inner_triangle2)

        outer_triangle3 = [inner_triangle[2], inner_triangle[1], outer_triangle[2]]
        corner31 =  ((inner_triangle[2][0] + inner_triangle[1][0]) / 2,
                    (inner_triangle[2][1] + inner_triangle[1][1]) / 2)
        corner32 =  ((inner_triangle[1][0] + outer_triangle[2][0]) / 2,
                    (inner_triangle[1][1] + outer_triangle[2][1]) / 2)
        corner33 =  ((outer_triangle[2][0] + inner_triangle[2][0]) / 2,
                    (outer_triangle[2][1] + inner_triangle[2][1]) / 2)
        inner_triangle3 = [corner31, corner32, corner33]
        sierpinski_aux(pen, stop_index-1, outer_triangle3, inner_triangle3)


def sierpinski(stop_index):

    turtle.TurtleScreen._RUNNING = True # Necessary for Tkinter recall... I don't know why???
    screen = turtle.Screen()
    pen = turtle.Turtle()
    pen.shape("circle")
    pen.shapesize(0.2, 0.2, 0.2)
    screen_width = screen.window_width()
    screen_height = screen.window_height()
    # pen.speed(1)

    corner_top = (0, screen_height/2 - 20)
    corner_left = (-screen_width/2 + 20, -screen_height/2 + 20)
    corner_right = (screen_width/2 - 20, -screen_height/2 + 20)
    outer_triangle = [corner_top, corner_left, corner_right]

    pen.up()
    pen.setpos(corner_top)
    pen.seth(270) # facing south
    pen.down()

    pen.setpos(corner_left)
    pen.setpos(corner_right)
    pen.setpos(corner_top)

    pos1 = ( (corner_top[0] + corner_left[0])/2, (corner_top[1] + corner_left[1])/2 )
    pos2 = ( (corner_left[0] + corner_right[0])/2, (corner_left[1] + corner_right[1])/2 )
    pos3 = ( (corner_top[0] + corner_right[0])/2, (corner_top[1] + corner_right[1])/2 )
    inner_triangle = [pos1, pos2, pos3]

    sierpinski_aux(pen, stop_index, outer_triangle, inner_triangle)

    screen.exitonclick()


if __name__ == "__main__":
    sierpinski(6)
