sal_bruto = float(input())
dep = int(input())

deducao = 0
INSS = 0

if sal_bruto <= 1372.82:
    aliquota = 0
elif sal_bruto <= 2743.25:
    aliquota = 0.15
    deducao = 205.92
elif sal_bruto > 2743.25:
    aliquota = 0.275
    deducao = 548.82
    
if sal_bruto <= 720:
    INSS = sal_bruto*0.0765
elif sal_bruto <= 1200:
    INSS = sal_bruto*0.09
elif sal_bruto <= 2400:
    INSS = sal_bruto*0.11
elif sal_bruto > 2400:
    INSS = 2400*0.11



IRRF = (sal_bruto - dep*137.99 - INSS)*aliquota - deducao

print ("{:.2f}".format(IRRF))