#Declaração de variáveis

xicaras, ovos, colheres = [int(w) for w in input().split()]

#Calculo

bolos = min(xicaras//2, ovos//3, colheres//5)

print (bolos)