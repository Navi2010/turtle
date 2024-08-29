import turtle
wn = turtle.Screen()
ted = turtle.Turtle()
wn.bgcolor("blue")
ted.pencolor("red")
ted.fillcolor("green")

ted.begin_fill()
for _ in range (6):
    ted.forward(60)
    ted.right(60)
ted.end_fill()


wn.exitonclick()