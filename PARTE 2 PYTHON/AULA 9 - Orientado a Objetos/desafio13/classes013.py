class Avaliacao():
    def __init__(self, nome = '', disciplina = '', nota = 0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    def set_nota(self,nota):
        if nota <= 10 and nota >= 0:
            self._nota = nota
        else:   
            print('valor invalido!')
    
    def get_nota(self):
        return self._nota