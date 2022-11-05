#Declaração de Variáveis

dist, dist_p_pedagio  = [float(w) for w in input().split()]

custo_p_km, custo_pedagio = [float(w) for w in input().split()]

#Viagem

custo_viagem = (dist//dist_p_pedagio)*custo_pedagio + dist*custo_p_km

print(round(custo_viagem))