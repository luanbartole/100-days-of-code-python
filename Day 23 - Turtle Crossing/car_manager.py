from turtle import Turtle
import random
COLORS = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
              (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]
MOVEMENT_INCREMENT = 10
STARTING_MOVE_DISTANCE = 5


class Car_Manager:

    def __init__(self):
        super().__init__()
        self.all_cars = []

    def create_cars(self):
        random_chance = random.randint(0, 5)
        if random_chance == 0:
            starting_y = random.randint(-200, 250)
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            new_car.setposition(300, starting_y)
            self.all_cars.append(new_car)

    def move_cars(self, level):
        for car in self.all_cars:
            car.forward(MOVEMENT_INCREMENT*(level/2))
