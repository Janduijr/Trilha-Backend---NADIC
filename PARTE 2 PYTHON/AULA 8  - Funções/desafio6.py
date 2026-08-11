def ajuda():
    condicao = ''
    while condicao != 'fim':
        print(f'sistema de ajuda python!')
        f = str(input('digite o nome da funcao: '))
        if f == 'fim':
            break
        print(f'acessando o manual do {f}')
        help(f)
        condicao = f
        
    
ajuda()
        
    