casa = int(input('QUAL O VALOR DA CASA? '))
salario = int(input('QUANTOS REAIS E O SALARIO? '))
tempo = int(input('EM QUANTOS ANOS VOCE QUER PAGAR A CASA? '))
mensalidade = casa/(tempo*12)

if mensalidade < (salario*0.30):
    print('EMPRESTIMO ACEITO!')
else:
    print('EMPRESTIMO NEGADO!')