#Declaração de Variáveis
n = int(input())
n_maria = 0

for nome in range (0, n):
    nome = input()
    nome = nome.split()
    
    if "Maria" in nome:
        n_maria += 1
        
print (n_maria)