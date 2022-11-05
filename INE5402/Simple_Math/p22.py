import math

#Declaração de Variáveis

x1, y1 = [float(w) for w in input().split()]

x2, y2 = [float(w) for w in input().split()]

#Calculo

distancia = math.sqrt((x2-x1)**2+(y2-y1)**2)

print("{:.4f}".format(distancia))