import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")

game = True

screen.tracer(0)

leftPaddle = Paddle(-380)
rightPaddle = Paddle(370)

ball = Ball()

leftScore = Scoreboard((-30, 250))
rightScore = Scoreboard((30, 250))

screen.listen()

screen.onkeypress(fun=leftPaddle.goUp, key="e")
screen.onkeypress(fun=leftPaddle.goDown, key="z")

screen.onkeypress(fun=rightPaddle.goUp, key="i")
screen.onkeypress(fun=rightPaddle.goDown, key=",")

while game:
    time.sleep(ball.moveSpeed)
    screen.update()
    ball.move()

    # detect collision with the top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounceWall()

    # detect collision with paddles
    if (ball.distance(leftPaddle) < 50 and ball.xcor() == -360) or (
        ball.distance(rightPaddle) < 50 and ball.xcor() == 350
    ):
        ball.bouncePaddle()

    # detect right missed collision
    if ball.xcor() > 380:
        ball.resetPosition()
        leftScore.increaseScore()

    # detect left missed collision
    if ball.xcor() < -390:
        ball.resetPosition()
        rightScore.increaseScore()


screen.exitonclick()
