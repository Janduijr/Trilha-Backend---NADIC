class Pessoa:
    def __init__(self, nome = '', idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1
        
class Aluno(Pessoa):
    def __init__(self,nome,idade,curso,turma):
        super().__init__(nome,idade)
        self.curso = curso
        self.turma = turma
        
    def fazer_matricula(self):
        print(f'o aluno {self.nome} acabou de fazer a sua matricula!')

class Professor(Pessoa):
    def __init__(self,nome,idade,especialidade,nivel):
        super().__init__(nome,idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'o professor {self.nome} acabou de dar aula!')

class Funcionario(Pessoa):
    def __init__(self,nome,idade,cargo,setor):
        super().__init__(nome,idade)
        self.cargo = cargo
        self.setor = setor
    
    def bater_ponto(self):
        print(f'o funcionario {self.nome} acabou de bater o ponto!')

aluno1 = Aluno('jandui',21,'ADS','4 periodo')
aluno1.fazer_aniversario()
print(aluno1.__dict__)
aluno1.fazer_matricula()

professor1 = Professor('Aluisio',30,'Backend','Mestrado')
print(professor1.__dict__)

funcionario1 = Funcionario('Alex', 49, 'zelador', 'limpeza')
print(funcionario1.__dict__)