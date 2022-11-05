#Declaração de Variáveis
num = int(input())
val = 1
val_ant = 0
val_ant_2 = 0

#Calculo do valor
for posicao in range (2, num + 1):
    val_ant_2 = val_ant
    val_ant = val
    val = val_ant + val_ant_2
    
print (val)
    