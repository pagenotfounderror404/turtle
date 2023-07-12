from turtle import Turtle,Screen
from random import choice

t=Turtle()
s=Screen()
t.shape("turtle")
c=["red","blue","green","purple","yellow","brown","pink","black","crimson","orange"]
for i in range (3,11):
    for j in range(i):
        t.fd(100)
        t.left(360/i)
    r=choice(c)
    t.pencolor(r)
    c.remove(r)




s.exitonclick()