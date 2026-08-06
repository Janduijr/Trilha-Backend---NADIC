brasil = []
estados = {}
for x in range(0,3):
    estados['UF'] = str(input('digite a sigla: '))
    estados['nome'] = str(input('digite o nome do estado: '))
    brasil.append(estados.copy())

print(brasil)