matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = 0

for x in range(0,3):
    for y in range(0,3):
        matriz[x][y] = int(input(f'digite o valor {x}x{y}: '))
        if matriz[x][y] % 2 == 0:
            pares += matriz[x][y]

for x in range(0,3):
    for y in range(0,3):
        print(f'{matriz[x][y]:^5}', end='')
    print()

print('soma dos pares: ', pares)
print('soma da terceira coluna: ', matriz[0][2]+matriz[1][2]+matriz[2][2])
print('o maior valor segunda linha: ', max(matriz[1]))


