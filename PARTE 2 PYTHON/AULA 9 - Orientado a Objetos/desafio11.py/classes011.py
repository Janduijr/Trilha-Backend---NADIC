from abc import ABC, abstractclassmethod
from random import randint
class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = randint(0,3)
    
    def atacar(self,alvo,forca):
        if self.golpes == 0:
            self.golpes = 'chute'
        elif self.golpes == 1:
            self.golpes = 'soco'
        else:
            self.golpes = 'cabecada'
            
        print(f'{self.nome}({self.vida}) bateu em {alvo.nome}({alvo.vida}) com um {self.golpes} de forca {forca}')
        dano = randint(0,forca)
        alvo.receber_dano(dano)
        print(f'{alvo.nome} recebeu um dano de {dano}!')
    
    def receber_dano(self, dano):
        self.vida -= dano
    
    @abstractclassmethod
    
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
    
    def curar(self, vida):
        cura = randint(0,vida)
        self.vida += cura
        print(f'{self.nome} enrolou uma bandagem e teve uma cura de {cura} pontos de vida!')

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
    
    def curar(self, vida):
        cura = randint(0,vida)
        self.vida += cura
        print(f'{self.nome} tomou uma pocao de e obteve umaa cura de {cura} pontos de vida!')        