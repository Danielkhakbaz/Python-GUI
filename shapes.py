from turtle import Turtle, Screen
import random

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

    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)

    screen.colormode(255)

    print(turtle.pencolor(R, G, B))

    return turtle.pencolor(R, G, B)


def drawing_the_shapes(sides_number):
    """
    Drawing the shapes based on the sides number.
    """

    angle = 360 / sides_number

    change_color()

    for _ in range(sides_number):
        turtle.forward(100)
        turtle.right(angle)

# Drawing the shapes based on the side_number which it gets automatically in the range of 3 to 10
for side_number in range(3, 10):
    drawing_the_shapes(side_number)

# The window does not get closed until you click inside the window
screen.exitonclick()
