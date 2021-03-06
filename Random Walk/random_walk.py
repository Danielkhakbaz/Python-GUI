from turtle import Turtle, Screen
from random import randint, choice

directions = [0, 90, 180, 270]

turtle = Turtle()
screen = Screen()


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


# Set the screen size to the maximum
screen.setup(width=1.0, height=1.0)

# Change the speed of the pen
turtle.speed(10)

# Change the size of the pen
turtle.pensize(5)

# Drawing the random lines
for _ in range(50):
    change_color()
    turtle.forward(30)
    turtle.setheading(choice(directions))

# The window does not get closed until you click inside the window
screen.exitonclick()
