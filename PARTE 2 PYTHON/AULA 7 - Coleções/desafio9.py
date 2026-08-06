matriz = []
n = []
for x in range(0,3):
    for y in range(0,3):
        n.append(int(input(f'digite o valor {x}x{y}: ')))
    matriz.append(n[:])
    n.clear()
for x in range(0,3):
    print('{}'.format(matriz[x]))
     
        