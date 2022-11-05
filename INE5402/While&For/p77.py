#Declaração de Variáveis
n_jogadas = int(input())
Maria = 0
João = 0

#Calculo de Vitórias
while n_jogadas != 0:
    jogadas = input()
        
    Maria = jogadas.count("0")
    João = jogadas.count("1")
    
    print ("Mary won", Maria, "times and John won", João, "times")
    
    n_jogadas = int(input())