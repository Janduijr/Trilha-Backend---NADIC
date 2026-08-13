class Churrasco:
    def __init__(self, titulo = '', pessoas = 0):
        self.titulo = titulo
        self.pessoas = pessoas
        
    def analise(self):
        kg = 0.4*self.pessoas
        print('-'*45)
        print(f'{self.titulo: ^45}')
        print('-'*45)
        print('CADA PESSOA VAI COMER 400G DE CARNE - R$82.40/KG')
        print(f'recomendo comprar {kg}KG de carne!')
        print(f'o custo total sera de R${kg*82.40:.2f}')
        print(f'cada pessoa tera que pagar R${(kg*82.40)/self.pessoas:.2f}')
    

churrasco1 = Churrasco('churracao sexta!', 15)
churrasco1.analise()