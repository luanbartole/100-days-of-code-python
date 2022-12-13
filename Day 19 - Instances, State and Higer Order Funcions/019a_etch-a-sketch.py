from turtle import Turtle, Screen

# Creates the turtle and the screen
squirtle = Turtle()
screen = Screen()


# Functions with no arguments that control actions in the program.
def move_forward():
    squirtle.forward(10)


def move_backward():
    squirtle.backward(10)


def clockwise():
    squirtle.right(10)


def counter_clockwise():
    squirtle.left(10)


def clear():
    squirtle.clear()
    squirtle.penup()
    squirtle.home()
    squirtle.pendown()


# Event listener that allows the actions to be triggered when keys are hit.
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
