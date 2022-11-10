#Declaração das variáveis

dimensão = int(input())
P, Q, R, S, X, Y = [int(x) for x in input().split()]
I, J = [int(x) for x in input().split()]

Aij = 0
Bij = 0
Multiplicação = 0

for i in range (1, dimensão+1):
    Aij = (P*I + Q*i)%X
    Bij = (R*i + S*J)%Y
    Multiplicação += Aij * Bij

print(Multiplicação)