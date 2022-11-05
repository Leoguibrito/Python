#Declaração de Variáveis

alf_norm = input()
alf_cifr = input()

relacao = dict(zip(alf_cifr, alf_norm))

frase_cifr = input()
frase_norm = ''

for letra in frase_cifr:
    if letra in relacao:
        frase_norm += relacao[letra]
    else:
        frase_norm += letra
        
print (frase_norm)