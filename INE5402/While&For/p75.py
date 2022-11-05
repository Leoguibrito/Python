#Declaração de Variáveis
gabarito = input()
respostas = input()
questao = 0
acertos = 0

#Resultado
for letra in gabarito:
    if letra == respostas[questao]:
        acertos += 1
        questao += 1
    else:
        questao += 1

print (acertos)