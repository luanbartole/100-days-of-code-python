from turtle import Turtle, Screen
import random

# Define list of colors that will be used, extracted from image.jpg with colorgram module.
color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
              (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

# Sets the turtle and the screen
squirtle = Turtle()
screen = Screen()

# allows the screen to accept rgb colors in numeric tuples and sets the speed of the turtle.
screen.colormode(255)
squirtle.speed(500)

# Moving the cursor so it draws centralized.
squirtle.pu()
squirtle.setposition(-250, -200)


def hirst_painting():
    """Draws a line of 10 dots of random colors (Hirst Painting)"""
    for _ in range(0, 10):
        random_color = random.choice(color_list)
        squirtle.pu()
        squirtle.fd(50)
        squirtle.dot(20, random_color)
        squirtle.pd()

    squirtle.pu()
    squirtle.left(90)
    squirtle.fd(50)
    squirtle.right(90)
    position = squirtle.pos()
    squirtle.setposition(position[0] - 500, position[1] - 0)


for _ in range(0, 10):
    hirst_painting()
squirtle.hideturtle()

screen.exitonclick()
