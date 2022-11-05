import math

#Declaração de Variáveis

num = int(input())
Primo = (False)
divisor = num // math.sqrt(num)

#Verificação
if num > 1:
    while (num % divisor) > 0:
        divisor -= 1
    if divisor == 1:
        Primo = True

        
print (Primo)