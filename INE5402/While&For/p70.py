#Declaração de Varíaveis
casos = int(input())


while casos != 0:
    lados = 0
    retangulos = 0
    
#Calculo de Retangulos    
    for caso in range (0, casos):
        comp, quant = [int(w) for w in input().split()]
        lados += quant // 2
        
    retangulos = lados // 2
    
    print (retangulos)
    
    casos = int(input())