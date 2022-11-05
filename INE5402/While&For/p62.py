#Declaração de Variáveis
x = 1
xfat = 1

#Calculo do menor Inteiro
while xfat <= x**10:
    x += 1
    xfat = 1
    for fator in range (1, x+1):
        xfat *= fator

print (x)
