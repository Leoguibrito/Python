import math

#Declaração de variáveis
n = int(input())
val = []
media = 0
x = 0
m_total = 0

for a in range (0, n):
    num = float(input())
    val.append(num)
    m_total += num 

media = m_total/n

#Calculo do Desvio
for dado in val:
    x += (dado-media)**2
    
desvio = math.sqrt(x/(n-1))

print(desvio)