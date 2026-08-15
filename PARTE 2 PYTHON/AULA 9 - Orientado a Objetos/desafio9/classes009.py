from abc import ABC, abstractclassmethod
class Cafeteria(ABC):
    def __init__(self):
        pass
    
    def preparar(self):
        print('----iniciando preparo!----')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print('----pronto para beber!----\n')
        
    def ferver_agua(self):
        print('fervendo a agua a 100 graus.')
        
    @abstractclassmethod
    def misturar(self):
        pass
    def servir(self):
        pass

class Cafe(Cafeteria):
    def __init__(self):
        super().__init__()
    
    def misturar(self):
        print('mistura o cafe na cafeteira')
        
    def servir(self):
        print('serve o cafe em uma xicara grande')

class Cha(Cafeteria):
    def __init__(self):
        super().__init__()
    
    def misturar(self):
        print('mistura o cha na chaleira')
        
    def servir(self):
        print('serve o cha em uma xicara pequena')

class Leite(Cafeteria):
    def __init__(self):
        super().__init__()
    
    def misturar(self):
        print('mistura o leite em uma jarra')
    
    def servir(self):
        print('mistura o leite com o cafe ja pronto em uma xicara')