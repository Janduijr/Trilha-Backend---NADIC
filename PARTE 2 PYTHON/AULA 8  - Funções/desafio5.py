def notas(*n,sit):
    dicionario = {}
    maior = 0
    menor = 0
    soma = 0
    for x in range(0,len(n)):
        if x == 0:
            maior = n[x]
        else:
            if n[x] >= maior:
                maior = n[x]
        if  x == 0:
            menor = n[x]
        else:
            if n[x] <= menor:
                menor = n[x]
        soma += n[x]
    media = soma/len(n)
    dicionario['maior'] = maior
    dicionario['menor'] = menor
    dicionario['total'] = len(n)
    dicionario['media'] = media
    if sit == True:
        if media >= 6:
            dicionario['situacao'] = 'aprovados!'
        else:
            dicionario['situacao'] = 'reprovados!'
    return dicionario
sit = False
list = []
n = int(input('quantos alunos voce ira adicionar? '))     
for x in range(0,n):
    list.append(float(input(f'nota do aluno {x}: ')))

print('1 - Mostrar situacao\n2 - Nao mostrar situacao')
s = int(input('resposta: '))
if s == 1:
    sit = True
elif s == 2:
    sit = False
else:
    print('resposta invalida!')
    
res = notas(*list,sit=sit)
print(res)