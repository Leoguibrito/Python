import math
#Declaração de variáveis

n = int(input())

primos_max = 1.25506*n/math.log(n)
primos_min = n/math.log(n)

print("{:.1f} {:.1f}".format(primos_min, primos_max))