#Declaração das variáveis
def linhas(x):
    Magico1 = True
    comparador = sum(matriz[0])
    for linha in matriz:
        somaL = sum(linha)
        if somaL != comparador:
            Magico1 = False
            break
    return Magico1

    
def colunas(x):
    somaC = 0
    Magico2 = True
    comparador = sum(matriz[0])
    for c in range (0, dimensão):
        for linha in matriz:
            somaC += linha[c]
        if somaC != comparador:
            Magico2 = False
            break
        somaC = 0       
    return Magico2

    
def diagonais(x):
    comparador = sum(matriz[0])
    somaDP = 0
    somaDS = 0
    Magico3 = True
    for linha in range (0, dimensão):
        for coluna in range (0, dimensão):
            if linha == coluna:
                somaDP += matriz[linha][coluna]
            if linha+coluna == dimensão-1:
                somaDS += matriz[linha][coluna]
    if somaDP != comparador or somaDS != comparador:
        Magico3 = False     
    return Magico3
     

dimensão = int(input())
matriz = []
QMagico = True

for l in range (0,dimensão):
    matriz += [([int(w) for w in input().split()])]
    
QMagico = linhas(matriz) and colunas(matriz) and diagonais(matriz)

print (QMagico)

    



