#Declaração de Variáveis
capital = float(input())
n_meses = float(input())
taxa_mes = float(input())

juros = (1 + taxa_mes/100)**(n_meses)

#Cálculo do Montante
montante = round((capital*juros), 2)

print(montante)