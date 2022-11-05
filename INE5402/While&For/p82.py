#Declarações de Variáveis
val_rom = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
num_rom = input()
num = 0
decimal = 0

#Conversão
while num < len(num_rom)-1:
    v1 = val_rom[num_rom[num]]
    v2 = val_rom[num_rom[num+1]]
    if v1 < v2:
        decimal += v2 - v1
        num += 2
    else:
        decimal += v1
        num += 1

if num+1 <= len(num_rom):
    decimal += val_rom[num_rom[-1]]

print (decimal)

    
        