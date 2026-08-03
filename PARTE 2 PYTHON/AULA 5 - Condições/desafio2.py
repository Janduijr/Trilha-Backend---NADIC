velocidade = int(input('A QUANTOS KM VOCE ESTA DIRIGINDO? '))

if velocidade > 80:
    print('VOCE ESTA ACIMA DA VELOCIDADE PERMITIDA!\nSUA MULTA: R$',(velocidade-80)*7)
else:
    print('PODE SEGUIR EM FRENTE!')