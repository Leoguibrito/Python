#Declaração de Variáveis

a = int(input())
b = int(input())

#Calculo

valor = abs(a-b+1)

if b>a:
    valor = abs(b-a+1)

print(valor)