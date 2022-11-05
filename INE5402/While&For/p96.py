#Declaração de Variáveis

n_carros, voltas = ([int(w) for w in input().split()])
Tvol = []
T_Ts = []

for carro in range (0, n_carros):
    Tvol = ([int(w) for w in input().split()])
    T_T = sum(Tvol)
    T_Ts += [T_T]
    
T_Ts_ord = sorted(T_Ts)
    
for tempo in T_Ts_ord[0:3]:
    print(T_Ts.index(tempo)+1)