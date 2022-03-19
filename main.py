from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
snake_colours=["red", "green", "blue"]
x_start_position = [0,20,40]
y_start_position = []
turtle_list=[]

for i in range(0,3):
    turtle = Turtle(shape="square")
    turtle.shapesize(1,1,1)
    turtle.color(snake_colours[i])
    turtle.write(i)
    turtle.penup()
    turtle.goto(x=x_start_position[i], y=0)
    print(turtle.position()[0])
    turtle_list.append(turtle)

print(turtle_list)


def forward():
    for j in range(3):
        # turtle_list[j].pendown()
        turtle_list[j].forward(50)

def backward():
    for j in range(3):
        # turtle_list[j].pendown()
        turtle_list[j].backward(50)

def left():
    turtle_list[2].left(90)
    turtle_list[2].forward(40)
    turtle_list[1].forward(20)
    turtle_list[1].left(90)
    turtle_list[1].forward(20)
    turtle_list[0].forward(40)
    turtle_list[0].left(90)

def right():
    turtle_list[2].right(90)
    turtle_list[2].forward(40)
    turtle_list[1].forward(20)
    turtle_list[1].right(90)
    turtle_list[1].forward(20)
    turtle_list[0].forward(40)
    turtle_list[0].right(90)


screen.update()
screen.onkey(forward,"w")
screen.onkey(backward,"s")
screen.onkey(left,"a")
screen.onkey(right,"d")

screen.listen()



screen.exitonclick()
screen.mainloop()