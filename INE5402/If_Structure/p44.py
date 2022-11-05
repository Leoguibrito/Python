dias = int(input())
km = int(input())

pt = 45*dias
extra = 0

if km > 60*dias:
    extra = (km - 60*dias)*0.5
    
pt += extra

print (pt)