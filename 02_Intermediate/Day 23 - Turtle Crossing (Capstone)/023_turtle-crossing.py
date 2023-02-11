import time
from turtle import Screen
from car_manager import Car_Manager
from player import Player
from scoreboard import Scoreboard

# Create the game window and properties.
screen = Screen()
screen.title("Turtle Crossing by Luan Bartole")
screen.setup(width=600, height=600)
screen.colormode(255)
screen.tracer(0)

# Create objects for the game
player = Player()
car_manager = Car_Manager()
scoreboard = Scoreboard()

# Set key listener to trigger player's action
screen.listen()
screen.onkeypress(player.move_up, "Up")

# Turtle Crossing Game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generate cars and move them
    # Generate more cars each time the difficulty_level goes up every 3 levels.
    difficulty_level = round(scoreboard.level / 3) + 1
    for _ in range(0, difficulty_level):
        car_manager.create_cars()
    car_manager.move_cars(scoreboard.level)
    # Collision with upper wall - Level Up
    if player.ycor() > 280:
        scoreboard.increase_score()
        player.goto(player.xcor(), -250)

    # Collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
