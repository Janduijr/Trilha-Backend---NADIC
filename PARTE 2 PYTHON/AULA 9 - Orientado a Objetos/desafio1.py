class Funcionario:
    def __init__(self, nome = 'desconhecido', setor = 'desconhecido', cargo = 'desconhecido'):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
        
    def __str__(self):
        return f'ola me chamo {self.nome}, ocupo o cargo {self.cargo} do setor de {self.setor}!'
    

funcionario1 = Funcionario('jandui', 'vendas', 'gerente')
print(funcionario1)
funcionario2 = Funcionario(setor='reposicao', cargo = 'repositor')
print(funcionario2)