frase = input()

while frase != '*':
    frase = frase.lower()
    letra1 = frase[0]
    frase = frase.split()
    for palavra in frase:
        if palavra[0] == letra1:
            Tautogramas = 'Y'
        else:
            Tautogramas = 'N'
            break
    
    print (Tautogramas)
    frase = input()