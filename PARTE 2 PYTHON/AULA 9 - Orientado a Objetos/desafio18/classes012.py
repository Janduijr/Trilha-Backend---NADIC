import hashlib

class Banco:
    def __init__(self, id = 0, nome = 'desconhecido', saldo = 0):
        self._id = id
        self._nome = nome
        self.__saldo = saldo
        self.__hash = None
        
    def __str__(self):
        return f'A conta de {self._nome} codigo {self._id} possui R${self.__saldo:.2f} senha: {self.__hash}'
        
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
    
    def pede_senha(self):
        senha = str(input('Digite a senha: '))
        senha = senha.encode('utf-8')
        hash = hashlib.sha256(senha).hexdigest()
        self.__hash = hash
        return self.__hash
    
