km = int(input('QUANTOS KM TEM A SUA VIAGEM? '))

if km > 200:
    print('ELA VAI CUSTAR: R$', km*0.45)
else:
    print('ELA VAI CUSTAR: R$', km*0.50)