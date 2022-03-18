from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
snake_colours=["white", "green", "blue"]
x_start_position = [0,20,40]
y_start_position = []

for i in range(0,3):
    turtle = Turtle(shape="square")
    turtle.color(snake_colours[i])
    turtle.penup()
    turtle.goto(x=x_start_position[i], y=0)
    print(turtle.position()[0])


















screen.exitonclick()