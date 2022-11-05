import math

#Declaração de Variáveis

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

#Calculo

pode_moverse = math.sqrt((x1-x2)**2+(y1-y2)**2) == math.sqrt(5)

print (pode_moverse)