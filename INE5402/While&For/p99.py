#Declaração de Variáveis
n_aero, voos = [int(x) for x in input().split()]
    Teste = 1

while (n_aero or voos) != 0:
    mais_cong = []
    aeroporto = [0]*n_aero
    for voo in range (0, voos):
        emb, des = [int(x) for x in input().split()]
        aeroporto[emb-1] += 1
        aeroporto[des-1] += 1
    
    maior_cong = aeroporto[0]
    aero = 1
    
    for cong in aeroporto:
        if cong == maior_cong:
            mais_cong.append(aero)
            aero += 1
        elif cong > maior_cong:
            maior_cong = cong
            mais_cong = [aero]
            aero += 1
        else:
            aero += 1
    
    mais_cong.sort()
    n_aero, voos = [int(x) for x in input().split()]
    
    if (n_aero and voos) == 0:
        print ('Teste', (Teste))
        print (*mais_cong)
    else:
        print ('Teste', (Teste))
        print (*mais_cong, '\n')
    
    Teste += 1


        

