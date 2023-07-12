import random
from turtle import Turtle,Screen

t=Turtle()
s=Screen()
t.shape("turtle")
s.colormode(255)
def color():
    r=random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    c=(r,g,b)
    return c

for i in range (360):
    t.pencolor(color())
    t.circle(100)
    t.rt(i+1)

s.exitonclick()