from random import randint
computador = randint(1,3)
print('1 - pedra\n2 - tesoura\n3 - papel')
eu = int(input('sua escolha: '))

if computador == eu:
    print('empatou!')
elif computador == 1 and eu == 3 or computador == 2 and eu == 1 or computador == 3 and eu == 2:
    print('voce ganhou!')
    if computador == 1:
        print('computador era pedra!')
    elif computador == 2:
        print('computador era tesoura!')
    else:
        print('computador era papel!')
else:
    print('voce perdeu!')
    if computador == 1:
        print('computador era pedra!')
    elif computador == 2:
        print('computador era tesoura!')
    else:
        print('computador era papel!')