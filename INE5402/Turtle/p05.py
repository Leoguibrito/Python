import turtle
import math

t = turtle.Turtle()

razao = 5
t.color("Orange")
t.forward(100)
t.fillcolor('Orange')
for raio in range(10, 50, razao):
    t.begin_fill()
    t.circle(raio)
    t.end_fill()
    
    t.up()
    t.forward(2*raio + razao)
    t.down()
   
      
turtle.done()
