class Pessoa:
    def __init__(self):
        self.nome = ''
        self.idade = 0
        
    def aniversario(self):
        self.idade += 1
    
    def fala(self):
        return f'ola me chamo {self.nome} e possuo {self.idade} anos!'

obj = Pessoa()
obj.nome = 'jandui'
obj.idade = 21
obj.aniversario()
print(obj.fala())