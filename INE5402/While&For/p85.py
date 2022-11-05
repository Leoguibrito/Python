#Declaração de variáveis
alt_s, n_canos = [int(w) for w in input().split()]
alt_cano = [int(w) for w in input().split()]



for cano in alt_cano:
    if abs(cano-alt_s) <= alt_s:
        res = 'YOU WIN'
    else:
        res = 'GAME OVER'
        break
    
print (res)

