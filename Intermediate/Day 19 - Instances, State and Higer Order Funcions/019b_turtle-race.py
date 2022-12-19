import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
all_turtles = []
screen = Screen()
screen.setup(width=500, height=400)

bet = screen.textinput("Make a bet", "What color is the winning turtle?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=130 - turtle_index * 50)
    all_turtles.append(new_turtle)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == bet:
                print(f"You Won! The winning turtle was the [{winning_turtle}]")
            else:
                print(f"You lost! The winning turtle was the [{winning_turtle}]")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
