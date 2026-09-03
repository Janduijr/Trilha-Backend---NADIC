from hashlib import sha256

class Privado:
    def __init__(self):
        self.__hash = None
    
    @property
    def senha(self):
        return self.__hash
    
    @senha.setter
    def senha(self,chave):
        if len(chave) > 0:
            self.__hash = sha256(chave.encode('utf-8')).hexdigest()
        else:
            print('Senha invalida!')
            
    def validar(self,chave):
        usuario = sha256(chave.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            print('senha confere!')
        else:
            print('senha errada!')