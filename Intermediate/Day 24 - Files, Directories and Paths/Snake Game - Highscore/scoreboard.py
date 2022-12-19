from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("courier", 16))

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", "w") as data:
                self.high_score = self.score
                data.write(f"{self.score}")
            self.refresh()
            self.score = 0
            self.refresh()

    def increase_score(self):
        self.score += 1
        self.refresh()
