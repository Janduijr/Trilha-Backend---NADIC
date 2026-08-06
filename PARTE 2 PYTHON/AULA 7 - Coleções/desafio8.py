#SEGUINDO PADRAO ATIVIDADE
matriz = []
n = []
for x in range(0,9): 
    n.append(int(input(f'digite o valor: ')))
    matriz.append(n[:])   
    n.clear()
    
for x in range(0,3):
    print('{}{}{}'.format(matriz[x], matriz[x+1], matriz[x+2]))