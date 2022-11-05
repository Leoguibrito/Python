#Declaração de Variáveis
n_participantes = int(input())
s1, s2, s3, nome = input().split()
s1 = float(s1)
s2 = float(s2)
s3 = float(s3)


#Descobrindo o Vencedor

nome_vit = nome

if s1 > s2 and s1 > s3:
    s_vit = s1
elif s2 > s3:
    s_vit = s2
else:
    s_vit = s3
    

for atleta in range(1, n_participantes):
    s1, s2, s3, nome = input().split()
    s1 = float(s1)
    s2 = float(s2)
    s3 = float(s3)  
    
    if s1 > s2 and s1 > s3 and s1 > s_vit:
        s_vit = s1
        nome_vit = nome
    elif s2 > s3 and s2 > s_vit:
        s_vit = s2
        nome_vit = nome
    elif s3 > s_vit:
        s_vit = s3
        nome_vit = nome
        
print (nome_vit)
    
        