import math

#Declaração de Variáveis
a = int(input("Digite a: "))
b = int(input("Digite b: "))
c = int(input("Digite c: "))
        
#Calcular Delta
delta = (b**2)-4*a*c

#Calcular as raízes
x1 = (-b + math.sqrt(delta))/(2*a)
x2 = (-b - math.sqrt(delta))/(2*a)

print("As raízes são: ", x1, "e ", x2)