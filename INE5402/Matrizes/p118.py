#Declaração de Variáveis

Qmatriz = int(input())
matriz = []

while Qmatriz != 0:
    for linha in range(0, Qmatriz):
        for coluna in range(0, Qmatriz):
            razão= 2**coluna
            matriz += [razão]
            
        print (matriz)
        matriz = []
    
    
    Qmatriz = int(input())