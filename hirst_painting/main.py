# import colorgram

# colours = colorgram.extract("image.jpg", 200)

# firstColour = colours[0]

# rgb = firstColour.rgb

# rgbColours = []

# for colour in colours:
#     red = colour.rgb.r
#     green = colour.rgb.g
#     blue = colour.rgb.b
#     rgbColours.append((red, green, blue))

# print(rgbColours)

import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

henry = Turtle()

colourList = [
    (231, 206, 83),
    (229, 147, 85),
    (119, 166, 186),
    (160, 13, 19),
    (30, 110, 159),
    (235, 81, 44),
    (5, 99, 37),
    (176, 19, 14),
    (187, 187, 25),
    (121, 177, 144),
    (207, 62, 22),
    (23, 132, 41),
    (245, 201, 4),
    (10, 42, 77),
    (13, 64, 41),
    (137, 83, 98),
    (83, 17, 24),
    (46, 168, 74),
    (3, 66, 140),
    (173, 133, 149),
    (36, 25, 21),
    (45, 151, 198),
    (220, 63, 68),
    (227, 171, 162),
    (73, 135, 188),
    (172, 204, 174),
    (216, 174, 178),
    (168, 201, 208),
    (177, 191, 211),
    (36, 73, 84),
    (248, 8, 15),
    (68, 64, 56),
    (253, 8, 5),
]

henry.penup()
initialX = -250
initialY = -250

for levels in range(10):
    henry.hideturtle()
    henry.speed(0)
    henry.setposition(initialX, initialY)
    for dots in range(10):
        henry.speed("slow")
        henry.dot(20, random.choice(colourList))
        henry.forward(50)
    initialY += 50


screen = Screen()

screen.exitonclick()
