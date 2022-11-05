#Declaração de variáveis
notas = [float(x) for x in input().split()]
notas.sort()

media = sum(notas[1:-1])

print(round(media, 1))