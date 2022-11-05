#Declaração de Variaveis
Dist = int(input())
Comb = float(input())

#Consumo
Cons = Dist/round(Comb, 1)

print("{:.3f}".format (Cons),"km/l")