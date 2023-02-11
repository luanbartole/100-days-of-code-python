import pandas
import turtle
from guess import Guess

screen = turtle.Screen()
screen.setup(width=1000, height=1000)
screen.title("Brazil States Game")
image = "brazil_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("brazil_states.csv")
guess = Guess(screen)


guess.quiz_the_user()
turtle.mainloop()