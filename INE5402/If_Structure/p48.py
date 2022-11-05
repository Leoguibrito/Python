VC = float(input())

desconto = VC*0.2

if VC >= 500 and VC < 1000:
    desconto = VC*0.3
elif VC >= 1000:
    desconto = 1000*0.3 + (VC - 1000)*0.45
    
custo = VC - desconto

print ("{:.2f}".format(custo))