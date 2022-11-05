#Declaração de Variáveis
t1 = int(input())
l1 = []

for a in range(0, t1):
    l1.append(input())
    
t2 = int(input())
l2 = []

for a in range(0, t2):
    l2.append(input())
    
#Lista Organizada
lista_completa = l1 + l2

lista_completa = sorted(lista_completa)

for nome in lista_completa:
    print(nome)