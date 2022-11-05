#Declaraçao de Variáveis

a, b = [int(w) for w in input().split()]

div1 = a%b == 0
div2 = b%a == 0

#Calculo

multiplo = "Nao sao Multiplos"

if div1 or div2:
    multiplo = "Sao Multiplos"

print(multiplo)