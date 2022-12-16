from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(coordinates[0], coordinates[1])
        self.pspeed = 20

    def up(self):
        self.goto(self.xcor(), self.ycor() + self.pspeed)

    def down(self):
        self.goto(self.xcor(), self.ycor() - self.pspeed)
