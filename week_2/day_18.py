# import  colorgram
#
# rgb_colors = []
# colors = colorgram.extract("hirst-image.jpg", 100)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random


screen = Screen()

color_list = [(15, 128, 179), (226, 153, 97), (194, 9, 27), (211, 229, 239), (34, 131, 71), (239, 207, 71), (212, 133, 156), (115, 181, 208), (207, 78, 103), (233, 77, 48), (152, 65, 109), (13, 171, 192), (206, 176, 14), (200, 8, 4), (39, 174, 143), (185, 69, 26), (125, 184, 153), (11, 101, 53), (243, 206, 4), (236, 160, 174), (243, 164, 151), (11, 43, 86), (142, 212, 225), (14, 56, 133), (80, 13, 39), (151, 215, 203), (11, 61, 35), (179, 182, 216), (123, 110, 175), (5, 91, 108), (95, 12, 7), (73, 99, 14), (250, 8, 19), (248, 11, 9)]
angle = [0, 90, 180, 270]

t = Turtle("turtle")
turtle.colormode(255)
screen.setworldcoordinates(-250, -200, screen.window_width() - 1, screen.window_height() - 1)
t.penup()

def make_dots():
    i = 0
    while i < 10:
        for _ in range(10):
            t.dot(20, random.choice(color_list))
            t.forward(50)
        if i % 2 == 0:
            t.setheading(90)
            t.forward(50)
            t.setheading(180)
            t.forward(50)
        elif i == 9:
            t.setheading(0)
        else:
            t.setheading(90)
            t.forward(50)
            t.setheading(0)
            t.forward(50)
        i += 1

make_dots()
screen.exitonclick()