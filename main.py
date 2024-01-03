# import turtle as t
import turtle
from turtle import Turtle , Screen
import random


# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("Red")

#Square in Turtle
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.shape("arrow")



# Draw a Dashed Lines

# jack = Turtle()
# for _ in range(15):
#     jack.forward(10)
#     jack.penup()
#     jack.forward(10)
#     jack.pendown()

# Drawing all shapes
# shape = Turtle()
# color=["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
#
#
#
# for i in range(3,11):
#     shape.color(random.choice(color))
#     num_sides = i
#
#
#     for _ in range(num_sides):
#         angle = 360/num_sides
#         shape.forward(100)
#         shape.right(angle)



# Random Walk
cat = Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    mytuple = (r,g,b)
    return mytuple

# color = ["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
directions = [0 , 90, 180 , 270]
cat.pensize(10)
cat.speed("fast")
#
for _ in range(200):
    # cat.color(random.choice(color))
    cat.color(random_color())
    cat.forward(30)
    cat.setheading(random.choice(directions))




screen = Screen()
screen.exitonclick()