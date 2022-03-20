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

turtle.done()