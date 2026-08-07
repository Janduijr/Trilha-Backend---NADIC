def mostranome(a):  
    print('--------------------')
    print(a)
    print('--------------------')
    
def soma(a, b):
    print(f'a soma de {a}+{b} e igual a {a+b}')
    
nome = str(input('digite o seu nome: '))
mostranome(nome)
a = int(input('digite o primeiro numero: '))
b = int(input('digite o segundo numero: '))
soma(a,b)