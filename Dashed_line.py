from turtle import Turtle,Screen
t=Turtle()
s=Screen()
t.color("blue")
t.shape("circle")
for i in range(30):
    t.pencolor("black")
    t.forward(10)
    t.pencolor("white")
    t.forward(10)

s.exitonclick()