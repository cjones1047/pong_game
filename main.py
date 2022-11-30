from turtle import Screen
from paddle import Paddle

# TODO Draw the table
# TODO Draw a left and right paddle
# TODO Draw the ball and make it move
# TODO Draw a scoreboard
# TODO Draw the vertical table separator down the center of the table

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
