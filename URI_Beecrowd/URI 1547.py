n = int(input("Quantidade de casos teste: "))
numeros = []
vencedores = []

for i in range(0, n):
    qt, s = [int(w) for w in input("Quantidade de alunos do grupo e número secreto: ").split()]
    numeros = [int(w) for w in input("Valores: ").split()]
    
    vencedor = 0
    menor_diferença = abs(numeros[0] - s) 
    for numero in numeros:
        diferença_atual = abs(numero-s)
        if diferença_atual < menor_diferença:
            vencedor = numeros.index(numero)
            menor_diferença = diferença_atual
    
    vencedores.append(vencedor+1)

for vencedor in vencedores:
    print (vencedor)