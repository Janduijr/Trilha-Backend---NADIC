class Gamer:
    def __init__(self, nome = 'desconhecido', nick = 'desconhecido'):
        self.nome = nome
        self.nick = nick
        self.favoritos = []
        
    def add_jogo(self, jogo):
        self.favoritos.append(jogo)
    def ficha(self):
        print('-'*30)
        print(f'Nick: {self.nick}')
        print(f'Nome real: {self.nome}')
        print('-'*30)
        print('jogos favoritos:')
        if len(self.favoritos) == 0:
            print('nao possui jogos favoritos!')
        else:
            for x in self.favoritos:
                print(x)
                
gamer1 = Gamer('jandui', 'Clashdragon')
gamer1.ficha()
gamer1.add_jogo('re4')
gamer1.ficha()
gamer1.add_jogo('LOL')
gamer1.ficha()



        