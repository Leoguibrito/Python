#Declaração de Variáveis

matriz = []
média_mensal = []

for mês in range (0,12):
    matriz = ([float(w) for w in input().split()])
    print(round(sum(matriz)/len(matriz),2), end = " ")