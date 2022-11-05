import math
#Declaração de Variáveis

pri = int(input())
ult = int(input())
Primos = 0


#Contagem de primos
for nat in range (pri, ult+1):
    divisor = nat // math.sqrt(nat)
    if nat > 1:
        while (nat % divisor) > 0:
            divisor -= 1
        if divisor == 1:
            Primos += 1
            
print (Primos)