from turtle import Turtle, Screen
tim=Turtle()
tim.color("red")
tim.shape("turtle")
for i in range(4):
    tim.fd(100)
    tim.left(90)
s=Screen()
s.exitonclick()