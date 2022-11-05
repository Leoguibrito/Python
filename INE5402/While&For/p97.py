#Declaração de Variáveis

frase = input().replace(' ', '').lower()

LMU = frase[0]
QLMU = frase.count(frase[0])

for letra in frase[1:]:
    if frase.count(letra) > QLMU:
        LMU = letra
        QLMU = frase.count(letra)
        
print (LMU)


