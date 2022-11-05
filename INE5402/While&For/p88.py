#Declaração de variáveis
ced_dif = int(input())
val = []
qtde = []
ced_us = []
i = -1

for n in range (0, ced_dif):
    val.append(float(input()))       
    qtde.append(int(input()))
    
saque = float(input())


#Calculo de uso
for ced in val[::-1]:
    resto = saque % ced
    if saque//ced > qtde[i]:
       resto += ced * ((saque//ced) - qtde[i])
       ced_us.append(int(qtde[i]))
    elif saque == 0 and saque//ced > qtde[i]:
        ced_us.append(int(saque//ced))
        break
    else:
        ced_us.append(int(saque//ced))
    saque = resto
    i += -1


print (*ced_us[::-1], ' ')
    
    
    