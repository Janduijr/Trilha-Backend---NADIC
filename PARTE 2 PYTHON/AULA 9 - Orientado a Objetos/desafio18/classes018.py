from hashlib import sha256
import hashlib

class Banco:
    def __init__(self, id = 0, nome = 'desconhecido', saldo = 0, senha = ''):
        self._id = id
        self._nome = nome
        self.__saldo = saldo
        self.__hash = sha256(senha.encode('utf-8')).hexdigest()
        usuario = sha256(''.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            print('Criando a conta...')
            self.pede_senha()
        
    def __str__(self):
        return f'A conta de {self._nome} codigo {self._id} possui R${self.__saldo:.2f}'
        
    def depositar(self):
        print('Realizando deposito:')
        n = int(input('quanto deseja depositar? '))
        n = abs(n)
        self.__saldo += n
    
    def sacar(self):
        print('Realizando saque:')
        senha = str(input('Digite a senha: '))
        usuario = sha256(senha.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            n = int(input('quanto deseja sacar? '))
            if n <= self.__saldo:
                n = abs(n)
                self.__saldo -= n
            else:
                print('saldo insuficiente!')
        else:
            print('Senha invalida!')
    
    def pede_senha(self):
        senha = str(input('Digite a senha: '))
        senha = senha.encode('utf-8')
        hash = hashlib.sha256(senha).hexdigest()
        self.__hash = hash
        return self.__hash
    
