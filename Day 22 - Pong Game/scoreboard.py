from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-100, 200)
        self.user_score = 0
        self.computer_score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.computer_score, align="center", font=("Courier", 60, "bold"))
        self.goto(100, 200)
        self.write(self.user_score, align="center", font=("Courier", 60, "bold"))

    def increase_user_score(self):
        self.user_score += 1
        self.refresh()

    def increase_computer_score(self):
        self.computer_score += 1
        self.refresh()
