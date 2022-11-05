#Declaração de Variáveis

valor = float(input())
sexo = input()
idade = int(input())

#Calculo

premio = valor*0.10

if sexo == "M":
    if idade <= 24:
        desconto = 0
    elif 24 < idade <= 33:
        desconto = 0.1
    elif idade > 33:
        desconto = 0.2
elif sexo == "F":
    if idade <= 24:
        desconto = 0.05
    elif 24 < idade <= 33:
        desconto = 0.2
    elif idade > 33:
        desconto = 0.35
        
seguro = premio - premio*desconto

print (seguro)