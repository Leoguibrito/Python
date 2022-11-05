#Declaração de Variáveis
cas_test = int(input())
div_sum = 0

for caso in range (0, cas_test):
    num = int(input())
    num_met = num // 2
    
    for divisor in range (1, num_met+1):
        if (num % divisor) == 0:
            div_sum += divisor
            
    if div_sum == num and num != 1:
        print (num, "eh perfeito")
        div_sum = 0
    else:
        print (num, "nao eh perfeito")
        div_sum = 0