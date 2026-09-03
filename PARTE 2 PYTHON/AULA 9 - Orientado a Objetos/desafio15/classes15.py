class Diario:
    def __init__(self, senha = '1234'):
        self.__segredo = []
        self.__senha = senha.strip()
    
    
    def escrever(self,mensagem):
        self.__segredo.append(mensagem.strip())
    
    def ler(self,senha):
        if self.__senha == senha:
            print('Abrindo diario:')
            for x in self.__segredo:
                print('-', x)
        else:
            raise PermissionError('Voce nao pode ler o diario!')
            
    @property
    def senha(self):
        raise PermissionError('Voce nao tem permissao!')

    @senha.setter
    def senha(self,novasenha):
        self.__senha = novasenha
        