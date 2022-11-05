#Declaração de Variáveis

eorigem = input()
torigem = float(input())
edestino = input()

if eorigem == edestino:
    tdestino = torigem
    
elif eorigem == "k":
    if edestino == "c":
        tdestino = torigem - 273.15
    elif edestino == "f":
        tdestino = (torigem - 273.15)*9/5 + 32
    elif edestino == "r":
        tdestino = torigem*1.8
    
elif eorigem == "c":
    if edestino == "k":
        tdestino = torigem + 273.15
    elif edestino == "f":
        tdestino = (torigem*9/5) + 32
    elif edestino == "r":
        tdestino = (torigem*9/5) + 459.67

elif eorigem == "f":
    if edestino == "c":
        tdestino = (torigem - 32)*5/9
    elif edestino == "k":
        tdestino = (torigem - 32)*5/9 + 273.15
    elif edestino == "r":
        tdestino = torigem + 459.67
    
elif eorigem == "r":
    if edestino == "c":
        tdestino = (torigem - 491.67)*5/9
    elif edestino == "k":
        tdestino = torigem*5/9
    elif edestino == "f":
        tdestino = torigem - 459.67
        
print (tdestino)