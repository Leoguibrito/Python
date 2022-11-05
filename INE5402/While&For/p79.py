#Declaração de Variáveis
n = input()
tamanho = len(n)
ponto = int(n.find('.'))
fst_n2 = tamanho

#Inteiros
if ponto < 0:
    if n[0] == '-':
        formatação = n[:2] + '.' + n[2:6] + 'E+' + str(tamanho-2).zfill(2)
    else:
        formatação = '+' + n[:1] + '.' + n[1:5] + 'E+' + str(tamanho-1).zfill(2)
    
#Frações
elif ponto > 0:
    #Frações abs > 0
    if n[0] == '-' and n[1] != '0':
        formatação = n[:2] + '.' + n[2:ponto] + n[ponto+1:7] + 'E+' + str(ponto-2).zfill(2)
    elif n[0] != '-' and n[0] != '0':
        formatação = '+' + n[:1] + '.' + n[1:ponto] + n[ponto+1:6] + 'E+' + str(ponto-1).zfill(2)
        
    #Frações abs < 0
    else:
        if n[0] == '-':
            for num in range (1, 10):
                fst_n = n.find(str(num))
                if fst_n2 > fst_n and fst_n != -1:
                    fst_n2 = fst_n
            formatação = '-' + n[fst_n2:fst_n2+1] + '.' + n[fst_n2+1:fst_n2+5].ljust(4,'0') + 'E-' + str(fst_n2-2).zfill(2)
        else:
            for num in range(1,10):
                fst_n = n.find(str(num))
                if fst_n2 > fst_n and fst_n != -1:
                    fst_n2 = fst_n
            formatação = '+' + n[fst_n2:fst_n2+1] + '.' + n[fst_n2+1:fst_n2+5].ljust(4,'0') + 'E+' + str(fst_n2-1).zfill(2)
            
        


print (formatação)