from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.increase_score()

    def increase_score(self):
        self.level += 1
        self.clear()
        self.goto(0, 250)
        self.write(f"Level:{self.level}", align="center", font=("Courier", 24, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Courier", 24, "bold"))
