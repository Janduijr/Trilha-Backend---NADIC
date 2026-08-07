def contador(*num):
    print(f'eu recebi os numeros: {num}\na tupla poussi: {len(num)} numeros')
def dobra(valores):
    for x in valores:
        print(f'o dobro de {x} e {x*2}')
valores = [5,5,4,3]
contador(1,5,3,8)
dobra(valores)