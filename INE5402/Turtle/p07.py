import turtle
import math

t = turtle.Turtle()

#Petalas Principais
for i in range(5):
    t.right(80)
    t.circle(140,100)
    t.left(80)
    t.circle(140,100)
    t.right(5+3*45)

t.right(30)
t.width(8)
t.forward(300)

#Petala Sec.
t.left(180)
t.forward(100)
t.right(90)
t.forward(6)

t.width(1)
t.circle(40,100)
t.left(80)
t.circle(40,100)


turtle.done()