aluno = {}
aluno['nome'] = str(input('digite o nome do aluno: '))
aluno['media'] = float(input('digite a media do aluno: '))
if aluno['media'] < 6:
    aluno['situacao'] = 'reprovado'
else:
    aluno['situacao'] = 'aprovado'

for k, v in aluno.items():
    print(f'{k} e igual {v}')
