sal = float(input())
sal_min = float(input())

x = sal/sal_min

if x <= 3:
    reajuste = sal*1.2
elif x > 3 and x <= 5:
    reajuste = sal*1.15
elif x > 5 and x <= 20:
    reajuste = sal*1.1
    
if reajuste <= 1.5*sal_min:
    reajuste = 1.5*sal_min
elif reajuste >= 20*sal_min:
    reajuste = 20*sal_min
    
print ("{:.2f}".format(reajuste))