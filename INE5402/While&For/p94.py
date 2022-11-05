#Declaração de Variáveis

sequencia = []
sequencia += ([int(w) for w in input().split()])
sequencia_ord = sorted(sequencia)


ordenação = 'N'

if sequencia == sequencia_ord:
    ordenação = 'C'  
elif sequencia == list(reversed(sequencia_ord)) :
    ordenação = 'D'
    
print (ordenação)