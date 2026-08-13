class Livro:
    def __init__(self, paginas = 0):
        self.paginas = paginas
        self.atual = 0
        
    def passarpagina(self):
        if self.atual < self.paginas:
            self.atual += 1
            print(f'VOCE PASSOU UMA PAGINA! PAGINA ATUAL: {self.atual}')
        else:
            print('VOCE CHEGOU AO FIM DO LIVRO!')
            
livro1 = Livro(5)
livro1.passarpagina()
livro1.passarpagina()
livro1.passarpagina()
livro1.passarpagina()
livro1.passarpagina()
livro1.passarpagina()
