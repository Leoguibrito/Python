#Declaração de Variáveis
n_calouros = int(input())
calouros = []
cal_doad = 0

for a in range(0, n_calouros):
    calouros.append(input())
    
n_doadores = int(input())
doadores = []

for a in range(0, n_doadores):
    doadores.append(input())
    
for nome in calouros:
    if nome in doadores:
        cal_doad += 1

relação = cal_doad/n_calouros