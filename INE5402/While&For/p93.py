#Declaração de Variáveis
tomada1 = []
tomada2 = []
N_e = 0

tomada1 = [int(w) for w in input().split()]
tomada2 = [int(w) for w in input().split()]


for entrada in tomada1:
    if tomada2[N_e] != entrada/1:
        compatível = "Y"
    else:
        compatível = "N"
    N_e += 1
        
print(compatível)

