import turtle
import random
from turtle import Turtle

turtle.colormode(255)
tim = Turtle()


def color_sett():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_circles(number):
    for num in range(int(360 / number)):
        start_heading = tim.heading()
        tim.color(color_sett())
        tim.circle(100)
        tim.setheading(start_heading + number)
tim.speed(0)
draw_circles(2)

screen = tim.screen
turtle.exitonclick()
