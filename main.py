import turtle

window = turtle.Screen()
draw = turtle.Turtle()

draw.color('#4048cd')
draw.fillcolor('#4048cd')
draw.begin_fill()
for i in range(4):
    draw.forward(300)
    draw.right(90)
draw.end_fill()

turtle.done()