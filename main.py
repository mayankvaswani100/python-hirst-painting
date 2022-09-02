import random
import colorgram
from turtle import Screen, Turtle, heading


screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.shape("turtle")

rgb_colors = []
colors = colorgram.extract('spot-painting.jpg', 20)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)


for counter in range(1, 100 + 1):
    random_color = random.choice(rgb_colors)
    tim.dot(20, random_color)
    tim.forward(50)

    if counter % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()
