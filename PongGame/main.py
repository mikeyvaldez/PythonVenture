#!/usr/bin/env python3


# - Create the screen
# - Create and move a padde
# -Create another paddle
# - Create the ball and make it move
# - Detect collision with wall and bounce
# - Detect collision with paddle
# - Detect when paddle misses
# - Keep score



from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen  = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with a wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce()

screen.exitonclick()

