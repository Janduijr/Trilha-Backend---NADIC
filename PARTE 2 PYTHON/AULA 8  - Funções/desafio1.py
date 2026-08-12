def fac(n=1):
    f = 1
    for x in range(n,0,-1):
        f*=x
    return f

n = int(input('digite um numero: '))
print(f'o fatorial de {n} e {fac(n)}!')