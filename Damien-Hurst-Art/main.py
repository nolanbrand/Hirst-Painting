import turtle as t
import random
from turtle import Screen

tim = t.Turtle()
t.colormode(255)


screen = Screen()
screen.setup(1000, 1000)
screen.setworldcoordinates(-1, -1, 20, 20)

tim.speed("fastest")
tim.hideturtle()

color_list = [(141, 163, 182), (14, 119, 185), (206, 138, 168), (199, 175, 9), (240, 213, 62), (220, 156, 97),
              (150, 17, 34), (122, 72, 100), (13, 143, 53), (74, 29, 35), (59, 34, 31), (204, 67, 26), (226, 170, 199),
              (242, 80, 27), (16, 172, 189), (34, 176, 93), (2, 114, 63), (247, 214, 2), (114, 188, 142),
              (181, 95, 111), (188, 182, 211), (40, 39, 46), (157, 207, 217), (229, 173, 162), (162, 208, 181),
              (118, 117, 163)]


def random_color(list_of_colors):
    return random.choice(list_of_colors)


def row_of_dots():
    for dot in range(20):
        tim.dot(20, random_color(color_list))
        tim.penup()
        tim.forward(1)
        tim.pendown()


def new_row(y_coord):
    tim.penup()
    tim.goto(0, y_coord)
    tim.pendown()


for row in range(20):
    row_of_dots()
    new_row(row + 1)

t.exitonclick()
