from turtle import Turtle ,Screen
import turtle
import random

cutie = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    mytuple = (r,g,b)
    return mytuple

cutie.speed("fastest")


for _ in range(int(360/5)):
    cutie.color(random_color())
    cutie.setheading(cutie.heading() + 10)
    cutie.circle(100)





screen = Screen()
screen.exitonclick()