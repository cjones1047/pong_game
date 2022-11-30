from turtle import Turtle, Screen

# TODO Draw the table
# TODO Draw a left and right paddle
# TODO Draw the ball and make it move
# TODO Draw a scoreboard
# TODO Draw the vertical table separator down the center of the table
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
SCREEN_BACKGROUND = "black"
SCREEN_TITLE = "Pong"
SCREEN_TRACE = 0

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(SCREEN_BACKGROUND)
screen.title(SCREEN_TITLE)
screen.tracer(SCREEN_TRACE)


screen.exitonclick()
