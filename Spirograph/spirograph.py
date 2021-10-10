from turtle import Turtle, Screen
from random import randint

turtle = Turtle()
screen = Screen()

# Set the screen size to the maximum
screen.setup(width=1.0, height=1.0)


def change_color():
    """
    Changing the color of the pen.

    Returns:
    a Method to change the color of the pen
    """

    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)

    screen.colormode(255)

    return turtle.pencolor(R, G, B)


# Change the speed of the pen
turtle.speed(0)


def draw_spirograph(size_of_gap):
    """
    Drawing many circles to make a spirograph.
    """
    for _ in range(int(360 / size_of_gap)):
        change_color()
        turtle.circle(120)
        turtle.setheading(turtle.heading() + size_of_gap)


draw_spirograph(6)

# The window does not get closed until you click inside the window
screen.exitonclick()
