#Declaração de Variáveis
dec = int(input())
binlst = []

#Divisão do Decimal
while (dec // 2) >= 0:
    if (dec // 2) > 0:
        binlst.append(dec % 2) 
        dec = dec // 2
    elif (dec // 2) == 0:
        binlst.append(dec % 2)
        break

#Formatação pra Binário
for bin_num in reversed (binlst):
    print (bin_num, end= '')