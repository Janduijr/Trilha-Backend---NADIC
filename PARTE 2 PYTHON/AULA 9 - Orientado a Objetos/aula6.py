from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome = ''):
        self.nome = nome
    
    @abstractmethod
    def emitir_som(self):
        pass
        

class Pato(Animal):
    def __init__(self, nome=''):
        super().__init__(nome)
    
    def emitir_som(self):
        print(f'{self.nome} e um {self.__class__.__name__} e esta gritando qua!')

class Cachorro(Animal):
    def emitir_som(self):
        print(f'{self.nome} e um {self.__class__.__name__} e esta latindo!')

class chihuahua(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} e um {self.__class__.__name__} e esta latindo 'AI! AI! AI!'")

class Pitbull(Cachorro):
    def emitir_som(self):
        print(f"{self.nome} e um {self.__class__.__name__} e esta latindo 'RUF! RUF! RUF!'")

class Gato(Animal):
    def emitir_som(self):
        print(f'{self.nome} e um {self.__class__.__name__} e esta miando!')

class Galinha(Animal):
    def emitir_som(self):
        print(f'{self.nome} e um {self.__class__.__name__} e esta cacarejando!')


animal1 = Pato('Donald')
animal1.emitir_som()
animal2 = Pitbull('Rex')
animal2.emitir_som()