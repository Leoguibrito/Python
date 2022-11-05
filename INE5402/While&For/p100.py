#Declaração de Variáveis
p_real, fre_nec = [int(w) for w in input().split()]


while p_real != 0 and fre_nec != 0:
    perguntas = [int(w) for w in input().split()]
    per_freq = 0
    for pergunta in set(perguntas):
        if perguntas.count(pergunta) >= fre_nec:
            per_freq += 1
    
    print (per_freq)
    
    p_real, fre_nec = [int(w) for w in input().split()]