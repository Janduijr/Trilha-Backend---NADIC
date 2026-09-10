class Carteira():
    def __init__(self, valor:int|float = 0):
        self.__saldo = valor

    @property
    def saldo(self):
        return f'O seu saldo e de R${self.__saldo}'
    
    @saldo.setter
    def saldo(self, valor):
        raise PermissionError('voce nao tem permissao!')
    
    def __eq__(self, outro):
        if self.__saldo == outro.__saldo:
            return  True
        else:
            return  False
    
    def __iadd__(self, valor: int|float = 0):
        self.__saldo += valor
        return self
        
        

c1 = Carteira(20)
print(c1.saldo)
c1 += 20
print(c1.saldo)

c2 = Carteira(30)
print(c1 == c2)

        