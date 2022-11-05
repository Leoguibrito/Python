import turtle
import math

t = turtle.Turtle()
raio1 = 110

t.width(2)
t.circle(raio1)

t.up()
t.left(90)
t.forward(110)
t.right(90)
t.down()

#Ponteiro Segundos
t.color('red')
t.left(120)
t.forward(80)
t.right(180)
t.forward(80)

#Ponteiro Minutos
t.width(4)
t.color('black')
t.left(100)
t.forward(65)
t.right(180)
t.forward(65)

#Ponteiro Horas
t.width(6)
t.left(60)
t.forward(50)
t.right(180)
t.forward(50)
t.right(190)

#Pontos
for i in range(12):
    t.up()
    t.forward(100)
    t.dot(6)
    t.right(180)
    t.forward(100)
    t.right(30)
    t.down()



      
turtle.done()
