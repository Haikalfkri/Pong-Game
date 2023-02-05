from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# r_paddle move
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")


# l_paddle move
screen.listen()
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


run = True
while run:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Collision with y
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    # Collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_score()

    #Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_score()

screen.exitonclick()