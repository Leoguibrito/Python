nota = float(input())

nota1 = nota % 1

if nota1 >= 0.25 and nota1 < 0.75:
    nota = nota - nota1 + 0.5
elif nota1 < 0.25 or nota1 >= 0.75:
    nota = round(nota)
    
print(nota)
