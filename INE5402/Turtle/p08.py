import turtle
import math

t = turtle.Turtle()
t.speed(11)

t.up()
t.left(90)
t.forward(140)
t.right(90)
t.down()

#Olhos
for i in range(2):
    t.right(90)
    t.fillcolor('Black')
    t.begin_fill()
    t.circle(40)
    t.end_fill()
    t.circle(80)
    t.circle(100)
    t.circle(120)

    t.up()
    t.right(90)
    t.forward(8)
    t.down()

t.up()
t.right(180)
t.forward(4)
t.left(90)
t.forward(200)
t.down()

#Nariz
for i in range(45):
    t.color('pink')
    t.width(2)
    t.forward(80)
    t.left(180)
    t.forward(80)
    t.right(4)
    
t.up()
t.left(45)
t.right(90)
t.forward(200)
t.left(90)
t.down()

#Boca
t.color('red')
t.width(10)
t.circle(200,100)

turtle.done()