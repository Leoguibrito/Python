#Declaração de Variáveis

tempo = int(input())

#Conversão

hora = tempo//3600
minutos = (tempo%3600)//60
seg = (tempo%3600)%60

print("{}:{}:{}".format(hora, minutos, seg))