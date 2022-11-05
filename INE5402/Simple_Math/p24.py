import math
#Declaração de Variáveis

lcontainer, ccontainer, hcontainer = [int(w) for w in input().split()]
lnavio, cnavio, hnavio = [int(w) for w in input().split()]

base = (lnavio//lcontainer) * (cnavio//ccontainer)
altura = hnavio//hcontainer

containers = base*altura

print(containers)