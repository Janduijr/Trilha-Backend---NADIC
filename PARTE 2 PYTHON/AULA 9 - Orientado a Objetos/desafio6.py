import os
class Controle:
    def __init__(self):
        self.estado = False
        self.volume = 50
        self.canal = 1
    
    def acao(self):
        '''
        precione @ para ligar e desligar
        precione > para passar canal
        precione < para voltar canal
        precione - para dimunir o volume
        precione + para aumentar o volume
        precione s para sair 
        '''
        
        os.system('cls' if os.name == 'nt' else 'clear')
        acao = ''
        while acao != 's':
            if self.estado == True:
                print('-'*30)
                print('A TV ESTA LIGADA!')
                print('-'*30)
                print(f'CH: ',{self.canal} )
                print(f'Vol: ', {self.volume}) 
                acao = str(input('O que deseja fazer? '))
                if acao == '>':
                    if self.canal == 5:
                        self.canal = 1
                    else:
                        self.canal += 1
                elif acao == '<':
                    if self.canal == 1:
                        self.canal = 5
                    else:
                        self.canal -=1
                elif acao == '+':
                    if self.volume == 100:
                        pass
                    else:
                        self.volume += 10
                elif acao == '-':
                    if self.volume == 0:
                        pass
                    else:
                        self.volume -= 10
                elif acao == '@':
                    if self.estado == True:
                        self.estado = False
                    else:
                        self.estado = True
                
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print('-'*30)
                print('A TV ESTA DESLIGADA!')
                print('-'*30)
                acao = str(input('O que deseja fazer? '))
                if acao == '@':
                    self.estado = True
                    os.system('cls' if os.name == 'nt' else 'clear')
                
            
            

tv1 = Controle()
help(tv1.acao)
input()
tv1.acao()

