#Declaração de Variáveis

ho =  ('0730', '0820', '0910', '1010', '1100', '1330', '1420', '1510', '1620', '1710', '1830', '1920', '2020', '2110')
dias = ('2', '3', '4', '5', '6', '7')


n_materias = int(input())

semana = {}


#semana['2']
#semana['2']['0730']
#semana['2']['0730'][0]


for n in range (0, n_materias):
    materia = input().split()
    for horario in materia[1:]:
        semana += {horario[0]:horario[1:]}
        