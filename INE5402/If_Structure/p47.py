A1 = int(input())
A2 = int(input())
A3 = int(input())

if A1 == A2 == A3:
    festas = 1
elif A1 != A2 and A2 != A3 and A1 != A3:
    festas = 3
else:
    festas = 2

print (festas)