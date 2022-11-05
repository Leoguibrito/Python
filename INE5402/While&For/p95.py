#Declaração de Variáveis

n_posto, di = [int(w) for w in input().split()]

p_postos = []
p_postos = ([int(w) for w in input().split()]) + [42195]

Tprova = 'S'

for posto in range(0, len(p_postos)-1):
    dp = p_postos[posto+1] - p_postos[posto]
    if dp > di:
        Tprova = 'N'
        break
        
print (Tprova)


    