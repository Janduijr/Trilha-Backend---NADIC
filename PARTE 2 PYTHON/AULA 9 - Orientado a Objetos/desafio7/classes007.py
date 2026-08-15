from abc import ABC, abstractclassmethod

class Pessoa(ABC):
    def __init__(self, nome = '', idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1
    
    @abstractclassmethod
    def estudar(self):
        pass
        
class Aluno(Pessoa):
    def __init__(self,nome,idade,curso,turma):
        super().__init__(nome,idade)
        self.curso = curso
        self.turma = turma
        
    def fazer_matricula(self):
        print(f'o aluno {self.nome} acabou de fazer a sua matricula!')
        
    def estudar(self):
        print('estudei 5 horas!')

class Professor(Pessoa):
    def __init__(self,nome,idade,especialidade,nivel):
        super().__init__(nome,idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'o professor {self.nome} acabou de dar aula!')
    
    def estudar(self):
        print('estudei 4 horas!')

class Funcionario(Pessoa):
    def __init__(self,nome,idade,cargo,setor):
        super().__init__(nome,idade)
        self.cargo = cargo
        self.setor = setor
    
    def bater_ponto(self):
        print(f'o funcionario {self.nome} acabou de bater o ponto!')
    
    def estudar(self):
        print('estudei 1 hora!')
