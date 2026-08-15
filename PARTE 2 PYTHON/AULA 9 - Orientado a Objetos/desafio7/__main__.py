from classes007 import Aluno, Funcionario, Professor


aluno1 = Aluno('jandui',21,'ADS','4 periodo')
aluno1.fazer_aniversario()
print(aluno1.__dict__)
aluno1.fazer_matricula()

professor1 = Professor('Aluisio',30,'Backend','Mestrado')
print(professor1.__dict__)

funcionario1 = Funcionario('Alex', 49, 'zelador', 'limpeza')
print(funcionario1.__dict__)
funcionario1.estudar()