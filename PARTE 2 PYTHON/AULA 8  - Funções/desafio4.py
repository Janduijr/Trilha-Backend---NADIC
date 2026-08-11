def leiaint(mensagem):
    val = True
    while val == True:
        n = input(mensagem)
        if n.isnumeric():
            val = False
            return n
        
        else:
            print(f'ERRO! digite um numero valido!')
            

            
            
num = leiaint('digite um numero: ')
print(f'o numero digitado foi {num}')
