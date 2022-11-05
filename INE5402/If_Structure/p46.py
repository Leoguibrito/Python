def equivalente_numerico(conceito):
    if conceito == "A":
        eqvnum = 4
    elif conceito == "B":
        eqvnum = 3
    elif conceito == "C":
        eqvnum = 2
    else:
        eqvnum = 0
    return eqvnum

tem_conceito_E = False
soma_eqvnum = 0
for _ in range(4):
    conceito = input()
    soma_eqvnum += equivalente_numerico(conceito)
    if conceito == "E":
        tem_conceito_E = True
        
ia = soma_eqvnum/4
esta_aprovado = not tem_conceito_E and ia >= 3

print(esta_aprovado)