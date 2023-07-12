from turtle import Turtle,Screen
from random import choice

t=Turtle()
s=Screen()
t.shape("turtle")
c=["red","blue","green","purple","yellow","brown","pink","black","crimson","orange","CornflowerBlue", "DarkOrchid",
   "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
score=[0, 90, 180, 270]
p=1.0
for i in range(50):
    color=choice(c)
    direction=choice(score)
    t.pencolor(color)
    t.setheading(direction)
    t.speed(p)
    t.width(p)
    t.fd(100)
    p+=0.5
s.exitonclick()
