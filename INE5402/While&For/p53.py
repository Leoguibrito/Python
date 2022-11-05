#Declaração de Variáveis

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

par = 0
impar = 0
positivo = 0
negativo = 0

for i in (n1, n2, n3, n4, n5):
    if i % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
    
    if i > 0:
        positivo = positivo + 1
    elif i < 0:
        negativo = negativo + 1
        
print (par, "valor(es) par(es)")
print (impar, "valor(es) impar(es)")
print (positivo, "valor(es) positivo(s)")
print (negativo, "valor(es) negativo(s)")