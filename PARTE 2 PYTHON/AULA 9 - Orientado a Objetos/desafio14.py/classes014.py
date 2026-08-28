class Termostato:
    def __init__(self):
        self.temperatura = 24
    
    @property
    def temperatura(self):
        return f'A temperatura esta em: {self._temperatura}'
    
    @temperatura.setter
    def temperatura(self, valor):
        if valor % 1 == 0 or valor % 1 == 0.5:
            if valor >= 16 and valor <= 30:
                self._temperatura = valor
            elif valor < 16:
                print('Temperatura informada invalida!')
                self._temperatura = 16
            elif valor > 30:
                print('Temperatura informada invalida!')
                self._temperatura = 30
            
            
        else:
            print('TEMPERATURA INVALIDA!')


