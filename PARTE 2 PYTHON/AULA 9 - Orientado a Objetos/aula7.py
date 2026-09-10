from functools import singledispatchmethod

class Analisador():
    
    @singledispatchmethod
    def analisar(self, valor):
        print(f'Nao foi possivel analisar o {valor}!')
    
    @analisar.register
    def _(self, valor : str):
        print(f'{valor} e uma str!')
        
    @analisar.register
    def _(self,valor:int):
        print(f'{valor} e um valor inteiro!')
    
    @analisar.register
    def _(self, valor: tuple|list|dict):
        print(f'{valor} e uma colecao de elementos!')

x = Analisador()
x.analisar([2,4,5])