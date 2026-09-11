from abc import ABC, abstractmethod
class Funcionario(ABC):
    def __init__(self, nome, valor):
        self.nome = nome
        self._salario = valor
        self.calcular_bonus()
        
    
    def __str__(self):
        return f'{self.nome} e um {self.__class__.__name__} e recebe {self.salario}'
    
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self):
        raise PermissionError('Voce nao tem permissao!')

    @abstractmethod
    def calcular_bonus(self):
        pass

class Gerente(Funcionario):
    def calcular_bonus(self):
        self._salario += self._salario*0.15

class Designer(Funcionario):
    def calcular_bonus(self):
        self._salario += self._salario*0.08
        

class Desenvolvedor(Funcionario):
    def calcular_bonus(self):
        self._salario += self._salario*0.10
        