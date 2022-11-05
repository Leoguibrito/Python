#Declaraçao de Variáveis

A = int(input())
B = int(input())
C = int(input())

#Calculo

triangulo = "isósceles"

if A==B==C:
    triangulo = "equilátero"
elif A!=B!=C!=A:
    triangulo = "escaleno"
    
print (triangulo)