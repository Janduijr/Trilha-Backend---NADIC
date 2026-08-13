class Pessoa:
    """
    Essa classe cria uma pessoa com nome e idade!
    """
    def __init__(self,nome = '',idade = 0):
        self.nome = nome
        self.idade = idade
        
    def aniversario(self):
        self.idade += 1
    
    def __str__(self):
        return f'ola me chamo {self.nome} e possuo {self.idade} anos!'
    
    def __getstate__(self):
        return f'Estado: Nome = {self.nome} Idade = {self.idade}'

obj = Pessoa('jandui', 21)
obj.aniversario()
print(obj.__doc__)
print(obj)
print(obj.__dict__) #dicionario nao formatado
print(obj.__getstate__()) #formatado
print(obj.__class__)