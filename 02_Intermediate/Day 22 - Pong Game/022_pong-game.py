import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game by Luan Bartole")
screen.tracer(0)

# Create the paddles, ball and score classes.
user_paddle = Paddle((350, 0))
computer_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.update()

# Set key listeners for player actions.
screen.listen()
screen.onkey(user_paddle.up, "Up")
screen.onkey(user_paddle.down, "Down")
screen.onkey(computer_paddle.up, "w")
screen.onkey(computer_paddle.down, "s")

# Pong Game
game_is_on = True
ball.setheading(55)
while game_is_on:
    screen.update()
    ball.move()

    # Collision with wall.
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    # Collision with paddle.
    if ball.distance(user_paddle) < 60 and ball.xcor() > 320 or ball.distance(computer_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()
        ball.bspeed *= 0.9
        user_paddle.pspeed += 2
        computer_paddle.pspeed += 2

    # Collision with user's wall.
    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x()
        user_paddle.pspeed = 20
        computer_paddle.pspeed = 20
        scoreboard.increase_computer_score()

    # Collision with computer's wall
    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.increase_user_score()

screen.exitonclick()
