from turtle import Turtle
import random

STARTING_MOVEMENTS = [10, -10]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.y_movement = random.choice(STARTING_MOVEMENTS)
        self.x_movement = random.choice(STARTING_MOVEMENTS)

    def move(self):
        if self.ycor() > 280 or self.ycor() < -270:
            self.y_movement *= -1
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)
