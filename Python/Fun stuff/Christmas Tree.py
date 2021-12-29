import turtle
import random
import time
width = 600
height = 500
window = turtle.Screen()
window.setup(width, height)
window.bgcolor("sky blue")
window.title("Merry Christmas")
snowball_rate = 1, 3
snowball_size = 5, 15
wind_change = 1, 5
max_wind = 3

list_of_snowballs = []


def make_snowball():
    snowball = turtle.Turtle()
    snowball.color("white")
    snowball.penup()
    snowball.setposition(random.randint(-2*width, width/2), height/2)
    snowball.hideturtle()
    snowball.size = random.randint(*snowball_size)
    list_of_snowballs.append(snowball)


def move_snowball(turtle_name, falling_speed=1, wind=0):
    turtle_name.clear()
    turtle_name.sety(turtle_name.ycor() - falling_speed)
    if wind:
        turtle_name.setx(turtle_name.xcor() + wind)
    turtle_name.dot(turtle_name.size)

import turtle
screen = turtle.Screen()
screen.setup(800,1000)
circle = turtle.Turtle()
circle.shape('circle')
circle.color('red')
circle.speed('fastest')
circle.up()
square = turtle.Turtle()
square.shape('square')
square.color('green')
square.speed('fastest')
square.up()
circle.goto(0,280)
circle.stamp()
k = 0
for i in range(1, 17):
    y = 30*i
    for j in range(i-k):
        x = 30*j
        square.goto(x,-y+280)
        square.stamp()
        square.goto(-x,-y+280)
        square.stamp()
    if i % 4 == 0:
        x = 30*(j+1)
        circle.color('red')
        circle.goto(-x,-y+280)
        circle.stamp()
        circle.goto(x,-y+280)
        circle.stamp()
        k += 2
    if i % 4 == 3:
        x = 30*(j+1)
        circle.color('yellow')
        circle.goto(-x,-y+280)
        circle.stamp()
        circle.goto(x,-y+280)
        circle.stamp()
square.color('brown')
for i in range(17,24):
    y = 30*i
    for j in range(3):
        x = 30*j
        square.goto(x,-y+280)
        square.stamp()
        square.goto(-x,-y+280)
        square.stamp()
text = turtle.Turtle()
text.color("deep pink")
text.penup()

#The code here may need you to modify the parameters to fit the position by setting the values in two "setposition" function.
text.setposition(10, 350)
text.write("Merry Christmas to xxx!", font=(
    "Apple Chancery", 30, "bold"), align="center")
#Enter your friend's name

text.setposition(130, 300)
text.color("red")
text.write("From xxx", font=("Avenir", 30, "bold"), align="right")
#Enter your name

text.hideturtle()    
time_delay = 0
start_time = time.time()
wind = 0
wind_delay = 5
wind_timer = time.time()
wind_step = 0.1
window.tracer(0)
while True:
    if time.time() - start_time > time_delay:
        make_snowball()
        start_time = time.time()
        time_delay = random.randint(*snowball_rate)/10
    for snowball in list_of_snowballs:
        move_snowball(snowball, wind=wind)
        if snowball.ycor() < -height/2:
            snowball.clear()
            list_of_snowballs.remove(snowball)
    if time.time() - wind_timer > wind_delay:
        wind += wind_step
        if wind >= max_wind:
            wind_step = -wind_step
        elif wind <= 0:
            wind_step = abs(wind_step)
        wind_timer = time.time()
        wind_delay = random.randint(*wind_change)/10
    window.update()
    turtle.exitonclick()
    break

turtle.Terminator()
