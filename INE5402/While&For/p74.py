#Declaração de Variáveis
CPF = input()
CPF = CPF.replace(".", "")
CPF = CPF.replace("-", "")

if CPF.count(CPF[0]) == 11:
    ver = False
else:
    #1º Dígito Verificador
    peso = 10
    soma = 0
    for num in CPF[:-2]:
        soma += int(num)*peso
        peso -= 1
    
    mod = 11 - (soma % 11)
    if mod == 10 or mod == 11:
        mod = 0
        
    ver = mod == int(CPF[-2])
    
    #2º Dígito Verificador
    peso = 11
    soma = 0
    for num in CPF[:-1]:
        soma += int(num)*peso
        peso -= 1
    
    mod = 11 - (soma % 11)
    if mod == 10 or mod == 11:
        mod = 0
    
    ver = mod == int(CPF[-1])
    
print (ver)