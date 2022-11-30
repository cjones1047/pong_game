from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.y_movement = 10
        self.x_movement = 10

    def move(self):
        if self.ycor() > 280 or self.ycor() < -270:
            self.y_movement *= -1
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)
