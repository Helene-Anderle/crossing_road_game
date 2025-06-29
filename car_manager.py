from random import randint, choice
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "grey"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(choice(COLORS))
            x_pos = 300
            y_pos = randint(-250, 250)
            new_car.goto(x_pos, y_pos)
            self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
