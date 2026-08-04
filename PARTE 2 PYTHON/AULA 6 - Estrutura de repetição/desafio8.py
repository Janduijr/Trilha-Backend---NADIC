senha = input('defina sua senha: ')
verificacao = ''
a = True
while a == True:
    
    verificacao = input('\nqual e a sua senha? ')
    
    if verificacao == senha:
        print('voce entrou!')
        a = False
    else:
        print('tente novamente!')
        True