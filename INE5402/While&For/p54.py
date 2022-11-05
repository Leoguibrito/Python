bandejas = int(input())
n = 0
Cquebrado = 0

while bandejas > n:
    L, C = [int(w) for w in input().split()]
    n = n + 1
    
    if L > C:
        Cquebrado = Cquebrado + C
    else:
        Cquebrado = Cquebrado
        
print (Cquebrado)