#Declaração de Variáveis

area = int(input())

#Número de galões e preço

galoes = max(1, round(area/64.8))
preço = galoes*25

#Saída

print("-área de cobertura: ", area)
print("-número de galões: ", galoes)
print("-valor a ser pago: R$ {:.2f}".format(preço))