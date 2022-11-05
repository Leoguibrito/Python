#Declaração de Variáveis
n_praias = int(input())
de15_20km = 0
dist_sum = 0

#1ª Praia
praia, distancia = input().split(';')
distancia = int(distancia)

dist_sum += distancia
maior_dist = distancia
p_mais_dist = praia

if distancia >= 15 and distancia <= 20:
    de15_20km += 1

#Calculo do Resultado
for praia in range (1, n_praias):
    praia, distancia = input().split(';')
    distancia = int(distancia)
    dist_sum += distancia
    
    if distancia >= 15 and distancia <= 20:
        de15_20km += 1
    
    if distancia > maior_dist:
        maior_dist = distancia
        p_mais_dist = praia
    
    
dist_med = round(dist_sum/n_praias, 1)

print ("{};{};{}".format(p_mais_dist, de15_20km, dist_med))
    
    
    