import turtle
from random import randint
from turtle import Turtle, Screen
import heroes

tim = Turtle()
# tom = Turtle()
# terry = Turtle()
tim.shape("turtle")
tim.color("ForestGreen")
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)


# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)
#
# tom.shape("circle")
# tom.color("blue")
# tom.right(180)
# for _ in range(3):
#     tom.forward(100)
#     tom.left(90)
#
# terry.right(90)
# terry.color("red")
# for _ in range(3):
#     terry.forward(100)
#     terry.left(100)
# print(heroes.gen())

# def dash(length, dash_leng):
#     for i in range(length // (dash_leng * 2)):
#         tim.pendown()
#         tim.forward(dash_leng)
#         tim.penup()
#         tim.forward(dash_leng)
# for _ in range(4):
#     dash(500, 10)
#     tim.right(90)

# circle = 360
# def challenge(sides):
#     degree = circle / sides
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(degree)
#
# colors_list = ["green", "blue", "purple", "red", "orange", "yellow", "tan", "grey"]
# i = 3
# c = 0
# while i <= 10:
#     tim.color(colors_list[c])
#     challenge(i)
#     i += 1
#     c += 1

# import random
#
# colors_list = ["green", "blue", "purple", "red", "orange", "yellow", "tan", "grey"]
# def walk(num):
#     i = 0
#     while i < num:
#         tim.color(colors_list[random.randint(0, 7)])
#         choose_turn = random.randint(1, 100)
#         if choose_turn >= 50:
#             tim.right(random.randint(0, 360))
#         else:
#             tim.left(random.randint(0, 360))
#         tim.forward(25)
#         i += 1
#
# walk(random.randint(1, 20))

# import random
# tim.pensize(10)
# tim.speed(10)
# colors_list = ["green", "blue", "purple", "red", "orange", "yellow", "tan", "grey"]
# def walk(num):
#     i = 0
#     while i < num:
#         tim.color(colors_list[random.randint(0, 7)])
#         choose_turn = random.randint(1, 100)
#         if choose_turn >= 50:
#             tim.right(90)
#         else:
#             tim.left(90)
#         tim.forward(35)
#         i += 1
#
# walk(random.randint(50, 100))

# import random
# tim.pensize(10)
# tim.speed("fastest")
# colors_list = ["green", "blue", "purple", "red", "orange", "yellow", "tan", "grey"]
# turtle.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
# direction = [0, 90, 180, 270]
# for _ in range(random.randint(100, 200)):
#     # tim.color(random.choice(colors_list))
#     tim.color(random_color())
#     tim.setheading(random.choice(direction))
#     tim.forward(35)

import random
# tim.pensize(10)
tim.speed("fastest")
colors_list = ["green", "blue", "purple", "red", "orange", "yellow", "tan", "grey"]
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def draw_spirograph(gap):
    for _ in range(int(360 / gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap)

draw_spirograph(2)









screen = Screen()
screen.exitonclick()