import turtle
import math

T = turtle.Turtle()

x = 100

T.begin_fill()
T.fillcolor('red')
T.forward(4*x)
T.left(90)
T.forward(2*x)
T.left(90)
T.forward(4*x)
T.left(90)
T.forward(2*x)
T.left(90)
T.end_fill()
T.forward(x/2)

T.up()
T.left(90)
T.forward(2*x/3)
T.down()

#Primeira Janela (A)
T.begin_fill()
T.fillcolor('black')
for i in range(4):
    T.forward(2*x/3)
    T.right(90)
T.end_fill()
#F1

T.up()
T.left(180)
T.forward(2*x/3)
T.down()

T.left(90)
T.forward(11*x/6)

#Porta
T.begin_fill()
T.fillcolor('cyan')
T.left(90)
T.forward(4*x/3)
T.left(90)
T.forward(2*x/3)
T.left(90)
T.forward(4*x/3)
T.end_fill()
#F2

T.left(90)
T.forward(7*x/6)

T.up()
T.left(90)
T.forward(2*x/3)
T.down()

#Segunda Janela (A)
T.begin_fill()
T.fillcolor('black')
for i in range(4):
    T.forward(2*x/3)
    T.right(90)
T.end_fill()
#F3

T.up()
T.forward(4*x/3)
T.left(90)
T.forward(x/2)
T.down()

T.forward(7*x/3)

#Telhado e Beiral
T.up()
T.left(30)
T.forward(x/6)
T.left(180)
T.down()

T.begin_fill()
T.fillcolor('orange')
T.forward(x/6 + 4*x*math.sqrt(3)/3)
T.right(60)
T.forward(x/6 + 4*x*math.sqrt(3)/3)
T.end_fill()
#F4

turtle.done()