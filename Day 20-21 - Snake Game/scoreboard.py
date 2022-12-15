from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("courier", 16))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("courier", 24, "bold"))

    def increase_score(self):
        self.score += 1
        self.refresh()
