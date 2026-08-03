a = int(input('digite o tamanho da primeira reta: '))
b = int(input('digite o tamanho da segunda reta:'))
c = int(input('digite o tamanho da terceira reta: '))

if a<b+c and b<a+c and c<a+b:
    if a==b==c:
        print('triangulo equilatero')
    elif a==b or b==c or a==c:
        print('triangulo isoceles')
    else:
        print('triangulo escaleno')
else:
    print('nao e um triangulo!') 