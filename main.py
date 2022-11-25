from turtle import Screen
import random
import turtle as t

t.colormode(255)
color_list = [(249, 248, 248), (238, 246, 243), (246, 240, 244), (235, 241, 246), (1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58), (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85), (145, 227, 216), (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179)]

tim = t.Turtle()
num_of_dots = 100
tim.penup()
for dot_count in range(1, num_of_dots):

    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()