#Declaração de Variáveis
tamanho = int(input())
int1 = int(input())
int2 = int(input())
menint = int1
menint2 = int2

#Calculo do 2º menor inteiro
if int2 < int1:
    menint = int2
    menint2 = int1

for inteiro in range (2, tamanho):
    int3 = int(input())
    if int3 <= menint2 and int3 >= menint:
        menint2 = int3
    elif int3 < menint2 and int3 < menint:
        menint2 = menint
        menint = int3
        
    

print (menint2)