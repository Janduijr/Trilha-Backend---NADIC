class Avaliacao():
    def __init__(self, nome = '', disciplina = '', nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota
    
    @property
    def nota(self):
        return self._nota
    
    @nota.setter
    def nota(self,valor):
        if valor <= 10 and valor >= 0:
                self._nota = valor
        else:   
            print('valor invalido!')

        

av1 = Avaliacao('jandui', 'matematica', 9.5)
av1.nota = 4.5
print(av1.nome, av1.disciplina, av1.nota)