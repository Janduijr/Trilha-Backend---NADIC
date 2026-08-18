class Banco:
    def __init__(self, nome = '', numero = 0, saldo = 0):
        self.nome = nome
        self._numero = numero
        self.__saldo = saldo
        
    def __str__(self):
        return f'A conta de {self.nome} codigo {self._numero} possui R${self.__saldo:.2f}'
        
    def depositar(self):
        n = int(input('quanto deseja depositar? '))
        n = abs(n)
        self.__saldo += n
    
    def sacar(self):
        n = int(input('quanto deseja sacar? '))
        if n <= self.__saldo:
            n = abs(n)
            self.__saldo -= n
        else:
            print('saldo insuficiente!')
    
