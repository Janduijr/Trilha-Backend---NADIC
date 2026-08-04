escolha = 11
n = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')
while escolha > 10:
    escolha = int(input('digite um numero: '))
    if escolha > 10:
        print('tente novamente! entre 0 e 10.')
print(f'{escolha}: {n[escolha]}')