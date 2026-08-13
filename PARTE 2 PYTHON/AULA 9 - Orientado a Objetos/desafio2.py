class Produto:
    def __init__(self, nome = 'desconhecido', preco = 'desconhecido'):
        self.nome = nome
        self.preco = preco
        
    def etiqueta(self):
        print(f'{self.nome: ^20}\n----------------------\n{self.preco: ^20}')
    

celular = Produto('iphone pro max', 2000)
celular.etiqueta()