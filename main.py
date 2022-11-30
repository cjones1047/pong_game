from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# TODO Draw the table
# TODO Draw a left and right paddle
# TODO Draw the ball and make it move
# TODO Draw a scoreboard
# TODO Draw the vertical table separator down the center of the table

LEFT_SCORE = 400
RIGHT_SCORE = -400

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

screen.listen()
screen.onkey(fun=l_paddle.go_up, key="w")
screen.onkey(fun=l_paddle.go_down, key="s")
screen.onkey(fun=r_paddle.go_up, key="Up")
screen.onkey(fun=r_paddle.go_down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # automatically detects ball's collision with wall and corrects course
    ball.move()

    # Detects collision with either paddle:
    if ball.xcor() == l_paddle.xcor() + 10 and ball.distance(l_paddle.position()) < 50:
        ball.x_movement *= -1
    elif ball.xcor() == r_paddle.xcor() - 10 and ball.distance(r_paddle.position()) < 50:
        ball.x_movement *= -1

    # Detects a score and resets the ball
    if ball.xcor() > LEFT_SCORE:
        ball.score_reset(scorer="left")
    elif ball.xcor() < RIGHT_SCORE:
        ball.score_reset(scorer="right")

screen.exitonclick()
