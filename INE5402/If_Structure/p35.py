#Declaração de Variáveis

N1 = float(input())
N2 = float(input())
N3 = float(input())

#Calculo

media = (N1 + N2 + N3)/3

nota = "Insuficiente"

if  7.5 > media >= 6:
    nota = "Satisfatório"
elif 9 > media >= 7.5:
    nota = "Bom"
elif media >= 9:
    nota = "Ótimo"
    
print (nota)
