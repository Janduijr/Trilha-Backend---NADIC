def fac(n,show=False):
    f = 1
    
    for x in range(n,0,-1):
        if show == True:
            print(x, end = '')
            if x > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= x
    
    else:
        return (f)

show = False
n = int(input('digite um numero: '))
m = int(input('1 - ver calculo \n2 - nao ver calculo\nsua resposta: '))

if m == 1:
    show = True
else:  
    show = False

print(fac(n, show))