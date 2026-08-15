from abc import ABC, abstractclassmethod
class Forma(ABC):
    
    @abstractclassmethod
    def perimetro(self):
        pass
    
    def area(self):
        pass

class Quadrado(Forma):
    def __init__(self,lado = 0):
        super().__init__()
        self.lado = lado
        
    def perimetro(self):
        print(f'um quadrado com lados de tamanho {self.lado} possui um perimetro de {self.lado*4:.1f}')
    
    def area(self):
        print(f'um quadrado com lado de tamanho {self.lado} possui uma area de {self.lado*self.lado:.1f}')

class Circulo(Forma):
    def __init__(self, raio):
        super().__init__()
        self.raio = raio
    
    def perimetro(self):
        print(f'um circulo com raio de tamanho {self.raio} possui um perimetro de {self.raio*6.28:.1f}')
    
    def area(self):
        print(f'um circulo com raio de tamanho {self.raio} possui uma area de {3.14*self.raio*self.raio:.1f}')

