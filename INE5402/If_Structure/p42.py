c = float(input())
l = float(input())
gav = int(input())
mad = input()

pc = c*l*100
pt = pc

if pc > 200:
    pt = pc + 50

if mad == "mogno":
    pt += 150
elif mad == "carvalho":
    pt += 125
    
pt += 30*gav

if pt < 200:
    pt = 200
    
print ("{:.2f}".format(pt))