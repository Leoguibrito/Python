#Declaração de variáveis
nome = input().split()
formatação = ''


for palavra in nome:
    if len(palavra) > 3 and not (palavra == nome[0] or palavra == nome[-1]):
        formatação += palavra[0] + '. '
    else:
        formatação += palavra + ' '

print(formatação)