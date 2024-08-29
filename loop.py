import turtle
wn = turtle.Screen()
dizzy = turtle.Turtle()
wn.bgcolor("light blue")
dizzy.pencolor("blue")
dizzy.speed(10)

side = 200
for _ in range (100):
    dizzy.forward(side)
    dizzy.right(90)
    side = side - 2

wn.exitonclick()
