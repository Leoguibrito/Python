#Declaração de Variáveis
tamanho = int(input())
int1 = int(input())
mai_int = int1
posicao = 1

for inteiro in range (1, tamanho):
    int2 = int(input())
    if int2 > mai_int:
        mai_int = int2
        posicao = inteiro + 1
        
print (mai_int, posicao)