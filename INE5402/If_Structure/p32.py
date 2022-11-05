#Declaração de Variáveis

C, P, F = [int(w) for w in input().split()]

serve = "N"

if P/(F*C) >= 1 :
    serve = "S"
    
print(serve)