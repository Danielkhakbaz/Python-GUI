from turtle import Turtle, Screen
from random import randint

screen = Screen()

# Set the screen size to the maximum
screen.setup(width=600, height=400)

all_the_turtles = []
is_race_on = True
COLORS = ["red", "orange", "yellow", "green", "blue", "violet", "pink"]
Y_DIRECTIONS = [-120, -80, -40, 0, 40, 80, 120]

user_bet = screen.textinput(
    title="Turtle Race!", prompt="Which turtle will win the race? Enter the color from the colors of the rainbow:")

for index, color in enumerate(COLORS):
    turtle = Turtle(shape="turtle")

    turtle.penup()
    turtle.color(COLORS[index])
    turtle.goto(-270, Y_DIRECTIONS[index])
    turtle.pendown()

    all_the_turtles.append(turtle)

while is_race_on:
    for turtle in all_the_turtles:
        if turtle.xcor() > 270:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You won! :)")
            else:
                print(f"You lost! {winning_color} won! :(")

        turtle.forward(randint(0, 20))

# The window does not get closed until you click inside the window
screen.exitonclick()
