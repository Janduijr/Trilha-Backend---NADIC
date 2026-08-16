from abc import ABC, abstractclassmethod
class Transporte(ABC):
    def __init__(self, distancia = 0):
        self.distancia = distancia
        self.frete = 0
    
    @abstractclassmethod
    def calc_frete(self):
        pass

class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 0.50
    
    def calc_frete(self):
        self.frete = self.distancia*self.fator
        return f'R${self.frete:.2f}'
    
class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 9.50

    def calc_frete(self):
        if self.distancia <= 10:
            self.frete = self.distancia*self.fator
            return f'R${self.frete:.2f}'
        else:
            return f'O maximo que o drone atende e 10KM'

class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)
        self.fator = 1.20
    
    def calc_frete(self):
        if self.distancia > 50:
            self.frete = self.distancia*self.fator
            return f'R${self.frete:.2f}'
        else:
            return f'O minimo de caminhao e 50km'


    
        
    