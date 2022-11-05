#Declaração de Variáveis
n_participantes = int(input())
participantes = []
Teste = 1

while n_participantes > 0:
    posição = 1
    participantes = ([int(w) for w in input().split()])
    n_participantes = int(input())
    
#Calculo do ganhador
    for ingresso in participantes:
        if ingresso == posição:
            ganhador = posição
            break
        else:
            posição += 1
        
    if n_participantes == 0:
        print ('Teste', Teste)
        print (ganhador)
    else:
        print ('Teste', Teste)
        print (ganhador)
        print ('')
    
    Teste += 1