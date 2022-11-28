from turtle import Turtle, Screen

MOVE_DISTANCE = 10
START_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]


class Snake:
    def __init__(self) -> None:
        self.segments = []
        self.screen = Screen()
        self.createSnake()

    def createSnake(self):
        for position in START_POSITIONS:
            self.snakeBody(position)

    def snakeBody(self, position):
        newSegment = Turtle("square")
        newSegment.shapesize(stretch_wid=0.5, stretch_len=0.5)
        newSegment.penup()
        newSegment.color("green")
        newSegment.goto(position)
        self.segments.append(newSegment)

    def move(self):
        self.screen.listen()
        for segmentTracker in range(len(self.segments) - 1, 0, -1):
            self.segments[segmentTracker].goto(
                self.segments[segmentTracker - 1].position()
            )
            self.segments[segmentTracker].setheading(
                self.segments[segmentTracker - 1].heading()
            )
        self.screen.onkey(fun=self.goUp, key="w")
        self.screen.onkey(fun=self.goDown, key="s")
        self.screen.onkey(fun=self.goLeft, key="a")
        self.screen.onkey(fun=self.goRight, key="d")
        self.segments[0].forward(MOVE_DISTANCE)

    def goUp(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def goDown(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def goLeft(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def goRight(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def extend(self):
        self.snakeBody(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(2000, 2000)
        self.segments.clear()
        self.createSnake()
