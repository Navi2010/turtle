import turtle
wn = turtle.Screen()
bob = turtle.Turtle()
wn.bgcolor("orange")
bob.pencolor("blue")


for _ in range(3):
    bob.forward(60)
    bob.left(120)

bob.penup()
bob.goto(0,30)
bob.pendown()

for _ in range(3):
    bob.forward(60)
    bob.right(120)

wn.exitonclick()