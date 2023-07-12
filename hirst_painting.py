import random
from turtle import Turtle,Screen
import colorgram

t=Turtle()
s=Screen()
t.shape("turtle")
s.colormode(255)
# c=colorgram.extract("image.jpg",30)
# rgbc=[]
# for i in c:
#    r=i.rgb.r
#    g = i.rgb.g
#    b = i.rgb.b
#    co=(r,g,b)
#    rgbc.append(co)
# print (rgbc)
score= "r"
c=[(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
t.speed("fastest")
t.penup()
t.goto(-200,-200)
def lineardot():
    for i in range(10):
        t.pendown()
        co = random.choice(c)
        t.dot(20, co)
        t.penup()
        t.fd(50)

t.hideturtle()
for i in range(10):
    p = t.pos()
    lineardot()
    # if d=='r':
    #     t.setheading(90)
    #     t.fd(50)
    #     t.setheading(0)
    #     d="l"
    # if d == 'l':
    #     t.setheading(90)
    #     t.fd(50)
    #     t.setheading(0)
    #     d = "r"
    t.setposition(p)
    t.penup()
    t.left(90)
    t.fd(50)
    t.right(90)
    t.pendown()

s.exitonclick()


