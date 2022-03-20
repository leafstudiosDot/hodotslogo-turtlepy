import turtle

window = turtle.Screen()
blue = turtle.Turtle()

blue.color('#4048cd')
blue.fillcolor('#4048cd')
blue.begin_fill()
for i in range(4):
    blue.forward(300)
    blue.right(90)
blue.end_fill()
blue.hideturtle()

red = turtle.Turtle()

red.penup()
red.goto(40, -40)
red.pendown()
red.color('#ee1d24')
red.fillcolor('#ee1d24')
red.begin_fill()
for i in range(4):
    red.forward(220)
    red.right(90)
red.end_fill()
red.hideturtle()

green = turtle.Turtle()

green.penup()
green.goto(80, -80)
green.pendown()
green.color('#22b14c')
green.fillcolor('#22b14c')
green.begin_fill()
for i in range(4):
    green.forward(140)
    green.right(90)
green.end_fill()
green.hideturtle()

turtle.done()