#Declaração de Variáveis
linhas, colunas = [int(w) for w in input().split()]
matriz = []

for linha in range (0, linhas):
    matriz += [[int(w) for w in input().split()]]
    
prod_max = sum(matriz[0])

for linha in matriz[1:]:
    if sum(linha) > prod_max:
        prod_max = sum(linha)

coluna = 0
val_col = 0
for coluna in range (0, colunas):
    for linha in range (0, linhas):
        val_col += matriz[linha][coluna]
    if val_col > prod_max:
        prod_max = val_col
    val_col = 0

print(prod_max)