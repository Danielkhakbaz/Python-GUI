from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

# Set the screen size to the maximum
screen.setup(width=1.0, height=1.0)

# Drawing the square
for _ in range(4):
    turtle.forward(100)
    turtle.left(90)

# The window does not get closed until you click inside the window
screen.exitonclick()
