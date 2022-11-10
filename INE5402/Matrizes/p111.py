#Declaração das variáveis
operação =  input()
total = 0

for linha in range (0, 12):
    for coluna in range(0,12):
        valor = float(input())
        if (coluna+linha) > 11:
            total += valor

if operação == 'M':
    print(round(total/66,1))
else:
    print(round(total,1))