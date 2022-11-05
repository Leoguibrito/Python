#Declaração de variáveis
notas = [float(x) for x in input().split()]
maior = notas[0]
menor = notas[0]

for num in notas:
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
        
media = sum(notas) - maior - menor

print(round(media, 1))