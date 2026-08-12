def voto(ano):
    i = 2026-ano
    if i < 18:
        return (f'voce possui {i} anos: NAO VOTA!')
    elif i >=18 and i < 65:
        return (f'voce possui {i} anos: O VOTO E OBRIGATORIO!')
    elif i >= 65:
        return (f'voce possui {i} anos: O VOTO E OPCIONAL!')
    else:
        return (f'ANO INVALIDO!')
    
idade = int(input('digite o ano em que voce nasceu: '))
print(voto(idade))