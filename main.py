from turtle import Screen, Turtle

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

left_paddle = Turtle()
left_paddle.color("white")
left_paddle.shape("square")
left_paddle.penup()
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.goto(-350, 0)
screen.update()


def go_up():
    new_y = left_paddle.ycor() + 20
    left_paddle.goto(left_paddle.xcor(), new_y)
    screen.update()


def go_down():
    new_y = left_paddle.ycor() - 20
    left_paddle.goto(left_paddle.xcor(), new_y)
    screen.update()


screen.listen()
screen.onkey(fun=go_up, key="Up")
screen.onkey(fun=go_down, key="Down")

screen.exitonclick()
