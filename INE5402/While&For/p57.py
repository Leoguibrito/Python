n = int(input())
primos = [2, 3, 5]

if n <= 1:
    eh_regular = False
else:
    for primo in primos:
        while n % primo == 0:
            n //= primo
            
    eh_regular = n == 1

print (eh_regular)
