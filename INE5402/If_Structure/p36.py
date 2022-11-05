#Declaração de Variáveis

valor = float(input())
classe = input()
origem = input()
idade = int(input())

premio = valor*0.15


if origem == "nacional":
    premio = valor*0.10


desconto1 = 0
    
if classe == "D":
    desconto1 = premio*0.05
elif classe == "C":
    desconto1 = premio*0.10
elif classe == "B":
    desconto1 = premio*0.20
elif classe == "A":
    desconto1 = premio*0.30


desconto2 = 0

if idade > 24:
    desconto2 = premio*0.10
    
seguro = premio - desconto1 - desconto2 

print(seguro)