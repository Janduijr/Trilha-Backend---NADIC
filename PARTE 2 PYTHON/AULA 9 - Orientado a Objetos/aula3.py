class banco:
    def __init__(self, nome = '', numero = 0, saldo = 0):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo
        
    def __str__(self):
        return f'A conta de {self.nome} codigo {self.numero} possui R${self.saldo:.2f}'
        
    def depositar(self):
        n = int(input('quanto deseja depositar? '))
        self.saldo += n
    
    def sacar(self):
        n = int(input('quanto deseja sacar? '))
        if n <= self.saldo:
            self.saldo -= n
        else:
            print('saldo insuficiente!')
    
jandui = banco('jandui', 132 , 20)
print(jandui)
jandui.depositar()
print(jandui)
jandui.sacar()
print(jandui)
