#Declaração de variáveis
cas_test = int(input())
val_ad = []

for caso in range (0, cas_test):
    qtde_al, num = [int(x) for x in input().split()]
    val_ad = ([int(w) for w in input().split()])
    ganhador = val_ad[0]
    
    for al in val_ad:
        if abs(al-num) < abs(ganhador-num):
            ganhador = al

print (val_ad.index(ganhador)+1)