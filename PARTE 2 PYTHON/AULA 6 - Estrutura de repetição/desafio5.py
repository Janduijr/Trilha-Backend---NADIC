a = True
while a == True:
    sexo = input('QUAL O SEU SEXO? M OU F? ')
    if sexo == 'M' or sexo == 'F':
        a = False
    else:
        a = True
        print('TENTE NOVAMENTE!')