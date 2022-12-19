from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Sets the screen and trace it.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by Luan Bartole")
screen.tracer(0)

# Create the snake, food and scoreboard classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Set key listeners for player actions.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Snake Game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_tail()
        screen.update()
        scoreboard.increase_score()

    # Collision with wall.
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()

    # Collision with tail.
    for segment in snake.snake_tail[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
