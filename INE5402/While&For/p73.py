#Declaração de Variáveis
palavra = input()
palavra2 = input()
Anagrama = False

#Anagrama
if len(palavra) == len(palavra2) and palavra != palavra2:
    for letra in palavra:
        Anagrama = (letra in palavra2)
        if Anagrama == False or palavra.count(letra) != palavra2.count(letra):
            Anagrama = False
            break
        
print (Anagrama)
    
