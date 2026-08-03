n = int(input('DIGITE UM NUMERO: '))
fatorial = 0
a = True

for x in range(n,0,-1):
    print(x)
    fatorial+=(n-1)*(n-2)
    if n == 1:
        a == False

        
print(f'o fatorial de {n} e {fatorial}!')