#Declaração de Variáveis
frase = input()


for letra in range (0, len(frase)):
    if frase[letra] == 'p' and frase[letra-1] != 'p':
        frase = list(frase)
        p = frase.pop(frase[letra])
        frase = "".join(frase)

print (frase)