#Declaração de Variáveis
h = int(input())
h_ex = int(input())

sal_b = 12.5*h + 15*h_ex
inss = sal_b*0.09
ir = sal_b*0.13

#Cálculo do Salário Líquido
sal_b = 12.5*h + 15*h_ex
sal_l = sal_b - ir - inss 


print("- Salário Bruto : R$ {:.2f}".format(sal_b))
print("- IR (13%) : R$ {:.2f}".format(ir))
print("- INSS (9%) : R$ {:.2f}".format(inss))
print("- Salário Líquido : R$ {:.2f}".format(sal_l))