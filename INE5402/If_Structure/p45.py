consumo = int(input())

if consumo <= 30:
    custo = consumo*0.09556
elif consumo <= 100:
    custo = 30*0.09556 + (consumo-30)*0.16698
elif consumo <= 200:
    custo = 30*0.09556 + 70*0.16698 + (consumo-100)*0.25052
elif consumo > 200:
    custo = 30*0.09556 + 70*0.16698 + 100*0.25052 + (consumo-200)*0.27836
    
print ("{:.2f}".format(custo))