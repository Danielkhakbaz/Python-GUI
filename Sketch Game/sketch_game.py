from turtle import Turtle, Screen, clear

turtle = Turtle()
screen = Screen()


def move_forward():
    """
    Move the pen forward by 10 pace.
    """
    turtle.forward(10)


def move_backward():
    """
    Move the pen backward by 10 pace.
    """
    turtle.backward(10)


def move_left():
    """
    Move the pen to the left by 10 pace.
    """
    turtle.left(10)


def move_right():
    """
    Move the pen to the right by 10 pace.
    """
    turtle.right(10)


def clear_the_painting():
    """
    Clear all the paintings.
    """
    turtle.clear()


# Set the screen size to the maximum
screen.setup(width=1.0, height=1.0)

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear_the_painting, "c")

# The window does not get closed until you click inside the window
screen.exitonclick()
