#Declaração de Variáveis

seq = int(input())
n = 1
media = 0

#Tarefa

while n < (seq + 1):
    an = float(input())
    media = media + an
    n = n + 1
    
media = media/seq

print (media)