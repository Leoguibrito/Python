#Declaração das variáveis
linha = int(input())
operação =  input()

total = 0


for l in range(0, 12):
    for coluna in range (0,12):
        valor = float(input())
        if l == linha:
            total += valor
            
if operação == 'M':
    print(round(total/12,1))
else:
    print(round(total,1))