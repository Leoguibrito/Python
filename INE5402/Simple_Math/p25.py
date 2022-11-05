#Declaração de Variáveis

idade_d1 = int(input())

#Conversão

idade_a = idade_d1//365
idade_m = (idade_d1%365)//30
idade_d2 = (idade_d1%365)%30

print(idade_a, "ano(s)")
print(idade_m, "mes(es)")
print(idade_d2, "dia(s)")
