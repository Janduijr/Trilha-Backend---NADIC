from classes15 import Diario

d1 = Diario('jandui')
d1.escrever('ola pessoal')
d1.escrever('tudo bem?')

try:
    d1.ler('jandui')
except Exception as e:
    print(f'ERRO: {e}')
