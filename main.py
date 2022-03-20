from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
snake_colours=["red", "green", "blue"]
x_start_position = [0,20,40]
y_start_position = []
turtle_list=[]
pen_y_position=250

def pen_write(text,pos):
    penTurtle = Turtle()
    penTurtle.pencolor("white")
    penTurtle.penup()
    penTurtle.goto(pos)
    penTurtle.pendown()
    penTurtle.write(text)



for i in range(0,3):
    turtle = Turtle(shape="square")
    turtle.shapesize(1,1,1)
    turtle.color(snake_colours[i])
    # turtle.write(i)
    turtle.penup()
    turtle.goto(x=x_start_position[i], y=0)
    print(turtle.position()[0])
    turtle_list.append(turtle)
    if i ==2:
        pen_write("starting", turtle_list[2].pos())

screen.update()

print(turtle_list)


def forward():
    for j in range(3):
        # turtle_list[j].pendown()
        turtle_list[j].forward(5)
        screen.update()
        # pen_write("forward")



def backward():
    for j in range(3):
        # turtle_list[j].pendown()
        turtle_list[j].backward(50)
        screen.update()


def left():
    time.sleep(0.1)
    turtle_list[2].left(90)
    pen_write("left", turtle_list[2].pos())
    turtle_list[2].forward(40)
    turtle_list[1].forward(20)
    turtle_list[1].left(90)
    turtle_list[1].forward(20)
    turtle_list[0].forward(40)
    turtle_list[0].left(90)
    screen.update()



def right():
    time.sleep(0.1)
    turtle_list[2].right(90)
    pen_write("right", turtle_list[2].pos())
    turtle_list[2].forward(40)
    turtle_list[1].forward(20)
    turtle_list[1].right(90)
    turtle_list[1].forward(20)
    turtle_list[0].forward(40)
    turtle_list[0].right(90)
    screen.update()




# screen.update()
# screen.onkey(forward,"w")
# screen.onkey(backward,"s")
# screen.onkey(left,"a")
# screen.onkey(right,"d")

screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    forward()
    screen.onkey(backward,"s")
    screen.onkey(left,"a")
    screen.onkey(right,"d")




screen.exitonclick()
screen.mainloop()