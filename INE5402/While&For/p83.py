import math

#Declaração de variáveis
n = int(input())
val = 1

for i in range (0,n):
    val *= float(input())
    
media_geométrica = val ** (1/n)

print (media_geométrica)