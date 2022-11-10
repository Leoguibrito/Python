#Declaração de Variáveis

n_matrizes = int(input())
matriz = []

for instancia in range (1, n_matrizes+1):
    for linha in range (0,9):
        matriz += [[int(w) for w in input().split()]]
        
    for linha in matriz:
        veri_lin = set(linha)
        if len(veri_lin) < 9:
            print('Instancia', instancia)
            print('NAO', \n)
            break
        
    for linha in range (0, len(matriz))
            