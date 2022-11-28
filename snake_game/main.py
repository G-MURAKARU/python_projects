from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=500, height=600)
screen.colormode(255)
screen.bgcolor((210, 213, 92))
screen.title("My Snake Game")
screen.tracer(0)

userName = screen.textinput(title="Player", prompt="Input username:").lower()
snake = Snake()
food = Food()
score = Scoreboard()

if userName == "highscore":
    with open("highscores.txt", mode="r") as scores:
        highScores = scores.read().rstrip()
        print(highScores)

else:
    game = True

    while game:
        screen.update()
        time.sleep(0.05)

        snake.move()

        # detects collision with food
        if snake.segments[0].distance(food) < 15:
            food.spawn()
            score.increaseScore()
            snake.extend()

        # detects collision with wall
        xCor = snake.segments[0].xcor()
        yCor = snake.segments[0].ycor()

        if xCor > 230 or xCor < -250 or yCor > 290 or yCor < -280:
            myScore = score.score
            score.reset()
            snake.reset()

        # detects collision with body
        for seg in snake.segments[1:]:
            if snake.segments[0].distance(seg) < 5:
                myScore = score.score
                score.reset()
                snake.reset()


screen.exitonclick()
