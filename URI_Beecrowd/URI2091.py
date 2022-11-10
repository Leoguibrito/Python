tamanho = int(input())

while (tamanho != 0):
    lista = [int(w) for w in input().split()]
    solitario = []
    for numero in lista:
        if numero in solitario:
            solitario.remove(numero) 
        else:
            solitario.append(numero)
    print(solitario[0])
    tamanho = int(input())
    