#Declaração de Variáveis
numero = input()
soma_pond = 0
peso = 2
num_inverso = numero[::-1]

#Calculo do Módulo
for digito in num_inverso[1:]:
    soma_pond += int(digito)*peso
    peso += 1


mod = 11 -(soma_pond % 11)
if mod == 10 or mod == 11:
    mod = 0

#Verificação
Verificado = mod == int(numero[-1])

print (Verificado)
   
   
