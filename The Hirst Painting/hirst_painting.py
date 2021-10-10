from turtle import Turtle, Screen
from colorgram import extract

turtle = Turtle()
screen = Screen()

# Set the screen size to the maximum
screen.setup(width=1.0, height=1.0)

# Set the color mode to RGB
screen.colormode(255)

turtle.penup()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
turtle.pendown()

colors = []
colors_pallete = extract("./hirst-painting.jpg", 30)

for color in colors_pallete:
    colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

for index, color in enumerate(colors):
    if (index + 1) % 10 == 0:
        turtle.penup()
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(360)
        turtle.pendown()

    turtle.dot(20, color)
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()

# The window does not get closed until you click inside the window
screen.exitonclick()
