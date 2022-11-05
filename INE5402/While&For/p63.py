#Declaração de Variáveis
tamanho = int(input())
int1 = int(input())
menint = int1

#Calculo do menor inteiro
for inteiro in range (1, tamanho):
    int2 = int(input())
    if int1 > int2:
        int1 = int2
        menint = int2
    
print(menint)