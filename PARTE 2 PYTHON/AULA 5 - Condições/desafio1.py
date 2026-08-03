from random import randint
computador = randint(0,5)
usuario = int(input('DIGITE UM NUMERO: '))

if usuario == computador:
    print('PARABENS VOCE VENCEU!')
else:
    print('INFELIZMENTE VOCE PERDEU! EU PENSEI NO ', computador)