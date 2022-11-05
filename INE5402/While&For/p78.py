#Declaração de Variáveis
frase = input()
frase2 = ''
espaço = 0

#Calculo dessa Desgraça
for letra in range (1, len(frase),2):
    if frase[letra-1] == ' ':
        espaço += 1
        frase2 += ' ' + frase[letra+espaço]
    elif frase[letra] == ' ':
        frase2 += ' '
        espaço -= 1
    else:
        frase2 += frase[letra+espaço]

    
print (frase2)