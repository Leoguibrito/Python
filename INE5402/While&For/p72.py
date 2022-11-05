#Declaração de Variáveis
frase = input()
frase_limpa = ''

#Verificação Palindromo
for letra in frase.lower():
    if letra.isalpha():
        frase_limpa += letra
    
fra_inv = frase_limpa[::-1]        
palind = frase_limpa == fra_inv

print (palind)