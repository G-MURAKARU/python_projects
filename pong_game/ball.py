from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()

        self.xMove = 10
        self.yMove = -10
        self.moveSpeed = 0.1

    def move(self):
        newXCor = self.xcor() + self.xMove
        newYCor = self.ycor() + self.yMove

        self.goto(newXCor, newYCor)

    def bounceWall(self):
        self.yMove *= -1

    def bouncePaddle(self):
        self.xMove *= -1
        self.moveSpeed *= 0.75

    def resetPosition(self):
        self.goto(0, 0)
        self.moveSpeed = 0.1
        self.xMove *= -1
