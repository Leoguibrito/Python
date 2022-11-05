#Declaração de Variáveis

sal_bruto = float(input())

INSS = sal_bruto*0.0765
    
if 720 < sal_bruto <= 1200:
    INSS = sal_bruto*0.09
elif 1200 < sal_bruto <= 2400:
    INSS = sal_bruto*0.11
elif 2400 < sal_bruto:
    INSS = 2400*0.11
    
print (INSS)
