from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVEMENT_SPEED = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.setposition(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVEMENT_SPEED)

