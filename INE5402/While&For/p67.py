#Declaração de Variáveis
massa = float(input())
tempo = 0

#Calculando tempo final
while massa >= 0.5:
    massa = massa / 2
    tempo += 50
    
print (tempo)